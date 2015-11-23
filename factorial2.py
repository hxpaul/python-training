#!/usr/bin/env python3

'''
output factorial of a number
'''

from __future__ import print_function

__copyright__ = 'Copyright 2015 Holiday Extras'
__licence__ = 'GPL'

import sys
import factorial

# if we didn't get exactly 2 arguments on the command line
# (the first one is the script name)
if len( sys.argv ) != 2:
  print( 'usage:', sys.argv[0], '[a number]' )
  exit( )

print( factorial.recursive( sys.argv[1] ))
print( factorial.iterative( sys.argv[1] ))
