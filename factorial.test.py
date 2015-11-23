#!/usr/bin/env python3

'''
tests for our factorial code
'''

__copyright__ = 'Copyright 2015 Holiday Extras'
__licence__ = 'GPL'

import unittest
from factorial import iterative
# instead of doing "import factorial"

class TestFactorial( unittest.TestCase ):
  def test_iterative_zero( self ):
    # if we'd just done "import factorial"
    # self.assertEqual( 1, factorial.iterative( 0 ));
    # but we imported just the function iterative so we can do:
    self.assertEqual( 1, iterative( 0 ));

  def test_iterative_negative_number( self ):
    self.assertRaises( ValueError, iterative, -66 );

  def test_iterative_number_we_know( self ):
    self.assertEqual( 5040, iterative( 7 ));

if __name__ == '__main__':
  unittest.main( )
