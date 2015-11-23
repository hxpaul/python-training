#!/usr/bin/env python3

'''
an example of inheritance
'''

__copyright__ = 'Copyright 2015 Holiday Extras'
__licence__ = 'GPL'

class StringStore( object ):
  def __init__( self, msg ):
    self.msg = msg

  # if you define __str__ this is called if you just print the object
  def __str__( self ):
    return self.msg

  def sayIt( self ):
    print( self.msg )

class HelloWorld( StringStore ):
  def __init__( self ):
    super().__init__( 'Hello world' )

# Always do this so we can use this as a script or as a module
if __name__ == '__main__':

  # this call creates an object that is a new instance of the class
  object = HelloWorld()
  object.sayIt()
  # you could also do HelloWorld().sayIt()
  # this one actually calls HelloWorld.__str__() if it is defined
  print( object ); 
