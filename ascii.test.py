#!/usr/bin/env python3

'''
tests for our ascii code
'''

__copyright__ = 'Copyright 2015 Holiday Extras'
__licence__ = 'GPL'

import unittest
from ascii import Square
from ascii import Rectangle
# instead of doing "import factorial"

class TestFactorial( unittest.TestCase ):
  def test_3_x_2_rectangle( self ):
    rectangle = '***\n***\n'
    self.assertEqual( rectangle, Rectangle( 3, 2 ).draw( ))
    self.assertEqual( rectangle, str( Rectangle( 3, 2 )))

  def test_3_x_2_rectangle( self ):
    rectangle = '***\n***\n'
    self.assertEqual( rectangle, Rectangle( 3, 2 ).draw( ))
    self.assertEqual( rectangle, str( Rectangle( 3, 2 )))

  def test_3_x_3_square( self ):
    rectangle = '***\n***\n***\n'
    self.assertEqual( rectangle, Square( 3 ).draw( ))
    self.assertEqual( rectangle, str( Square( 3 )))

if __name__ == '__main__':
  unittest.main( )
