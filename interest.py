#!/usr/bin/env python3

'''
This displays interest earned over a 10 year period,
at some fixed rates.
The first unassign string in a file (after the "from future") line
will be the description for the documentation!
'''

from __future__ import print_function, division

__copyright__ = 'Copyright 2015 Holiday Extras'
__licence__ = 'GPL'

import sys

years = 10
rates = ( 3, 5, 7 )

def compoundInterest( money, rate, year ):
  '''the compound interest earned'''
  return money * ( 1 + ( rate / 100 )) ** year

# Always do this so we can use this as a script or as a module
if __name__ == '__main__':

  if len( sys.argv ) != 2:
    print( 'usage:', sys.argv[0], '[amount of money]' )
    exit( )

  money = float( sys.argv[1] )

  for year in range( years ):
    row = [ ]
    for rate in rates:
      row.append( compoundInterest( money, rate, year ))
    print( '{:d}\t{:.2f}\t{:.2f}\t{:.2f}'.format( year + 1, *row ))
