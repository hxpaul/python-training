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

def compoundInterest( money, rate = 0, year = 1 ):
  '''the compound interest earned'''
  return money * ( 1 + ( rate / 100 )) ** year

# Always do this so we can use this as a script or as a module
if __name__ == '__main__':

  # if we didn't get exactly 2 arguments on the command line
  # (the first one is the script name)
  if len( sys.argv ) != 2:
    print( 'usage:', sys.argv[0], '[amount of money]' )
    exit( )

  # coerce our first arg, a string, to be a number
  money = float( sys.argv[1] )

  for year in range( 1, years + 1 ):
    row = [ ]
    for rate in rates:
      # row.append( compoundInterest( money, rate, year ))
      # or we can change the order
      row.append( compoundInterest( rate = rate, year = year, money = money ))
    print( '{:d}\t{:.2f}\t{:.2f}\t{:.2f}'.format( year, *row ))
