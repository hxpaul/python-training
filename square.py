#!/usr/bin/env python3

'''
ascii art - draw a square
'''

__copyright__ = 'Copyright 2015 Holiday Extras'
__licence__ = 'GPL'

import sys
from ascii import Square

if len( sys.argv ) != 2:
  print( 'usage:', sys.argv[0], '[side length]' )
  exit( )
print( Square( int( sys.argv[1] )))
