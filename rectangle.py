#!/usr/bin/env python3

'''
ascii art - draw a rectangle
'''

__copyright__ = 'Copyright 2015 Holiday Extras'
__licence__ = 'GPL'

import sys
from ascii import Rectangle

if len( sys.argv ) != 3:
  print( 'usage:', sys.argv[0], '[width] [height]' )
  exit( )
print( Rectangle( int( sys.argv[1], sys.argv[2] )))
