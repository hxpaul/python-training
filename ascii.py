#!/usr/bin/env python3

'''
ascii art
'''

__copyright__ = 'Copyright 2015 Holiday Extras'
__licence__ = 'GPL'

class Rectangle( object ):
  def __init__( self, width = 3, height = 2 ):
    self.width = width
    self.height = height

  def __str__( self ):
    return self.draw( )

  def draw( self ):
    output = ''
    for i in range( self.height ):
      for i in range( self.width ):
        output += '*'
      output += '\n'
    return output

class Square( Rectangle ):
  def __init__( self, size ):
    super( Square, self ).__init__( size, size )

# Always do this so we can use this as a script or as a module
if __name__ == '__main__':

  myRectangle = Rectangle( 5, 3 )
  print( myRectangle.draw( ))

  mySqure = Square( 5 )
  print( mySqure.draw( ))
