"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys
import thinkstats2
import nsfg

def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz'):

    dct = thinkstats2.ReadStataDct(dct_file, encoding='iso-8859-1')
    resp = dct.ReadFixedWidth(dat_file, compression='gzip')
    return resp

def CrossValidate(resp):
	preg = nsfg.ReadFemPreg()
	pregMap = nsfg.MakePregMap(preg)

	for caseid in resp['caseid']:
		if (len(pregMap[caseid]) != int(resp.loc[resp['caseid'] == caseid].pregnum)):
			print ("Test failed on caseid " + str(caseid) + ", pregMapNum: " + str(len(pregMap[caseid])) + ", respNum: " + str(resp.pregnum[caseid]))
			return False

	return True



def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    resp = ReadFemResp()

    assert(len(resp) == 7643)
    assert(resp.pregnum.value_counts()[1] == 1267)
    assert(resp.pregnum.value_counts()[2] == 1432)
    assert(resp.pregnum.value_counts()[3] == 1110)
    assert(CrossValidate(resp))

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)

# Failed on 5012
#resp.loc[resp['caseid'] == 5012]
