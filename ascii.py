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

  def fill( self, x, y, width, height ):
    if x == 0:
      return '*'
    if y == 0:
      return '*'
    if x == width - 1:
      return '*'
    if y == height - 1:
      return '*'
    return ' '

  def draw( self ):
    output = ''
    for i in range( self.height ):
      for j in range( self.width ):
        output += self.fill( j, i, self.width, self.height )
      output += '\n'
    return output

class Square( Rectangle ):
  def __init__( self, size ):
    super( Square, self ).__init__( size, size )
    # as we're using python3 we can just do
    # super( ).__init__( size, size )

# Always do this so we can use this as a script or as a module
if __name__ == '__main__':

  myRectangle = Rectangle( 5, 3 )
  print( myRectangle.draw( ))

  mySquare = Square( 5 )
  print( mySquare.draw( ))

  # this is bad
  mySquare = Square( 5 )
  mySquare.width = 20
  print( mySquare.draw( ))

