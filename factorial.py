#!/usr/bin/env python3

'''
output factorial of a number
'''

from __future__ import print_function
from functools import reduce
from operator import mul

__copyright__ = 'Copyright 2015 Holiday Extras'
__licence__ = 'GPL'

def _validate( n ):
  if not isinstance( n, int ):
    raise TypeError( 'can only do factorial of an integer' )
  if ( n < 0 ):
    raise ValueError( 'cannot do factorial of a negative number' )

def recursive( n ):
  '''recursively work out factorial, soon run out of space this way'''
  _validate( n )
  if n < 2:
    return 1
  return n * recursive( n - 1 )

def tailRecursive( n ) :
  '''tail recursive, still not good in python though'''
  _validate( n );
  if n < 2:
    return 1
  def iterate( i, result = 1 ):
    return result if i < 2 else iterate( i - 1, result * i )
  return iterate( n )

def usingReduce( n ):
  _validate( n )
  if n < 2:
    return 1
  return reduce( mul, range( 2, n + 1 ))

def iterative( n ):
  '''iteratively work out factorial, can work with bigger numbers'''
  _validate( n )
  i = 1
  result = 1
  while i <= n:
    result = result * i
    i += 1
  return result

# Always do this so we can use this as a script or as a module
if __name__ == '__main__':

  import sys

  # if we didn't get exactly 2 arguments on the command line
  # (the first one is the script name)
  if len( sys.argv ) != 2:
    print( 'usage:', sys.argv[0], '[a number]' )
    exit( )

  print( recursive( int( sys.argv[1] )))
  print( iterative( int( sys.argv[1] )))
  print( usingReduce( int( sys.argv[1] )))
