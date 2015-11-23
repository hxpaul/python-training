#!/usr/bin/env python3

'''
output factorial of a number
'''

from __future__ import print_function

__copyright__ = 'Copyright 2015 Holiday Extras'
__licence__ = 'GPL'

def recursive( n ):
  '''recursively work out factorial, soon run out of space this way'''
  n = int( float( n ))
  if n > 1:
    return n * recursive( n - 1 )
  return 1

def iterative( n ):
  '''iteratively work out factorial, can work with bigger numbers'''
  n = int( float( n ))
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

  print( recursive( sys.argv[1] ))
  print( iterative( sys.argv[1] ))
