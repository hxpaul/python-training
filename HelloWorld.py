#!/usr/bin/env python3

'''
an example of a calss
'''

__copyright__ = 'Copyright 2015 Holiday Extras'
__licence__ = 'GPL'

class HelloWorld( object ):
  def __init__( self ):
    self.msg = 'Hello world'

  # if you define __str__ this is called if you just print the object
  def __str__( self ):
    return self.msg

  def sayIt( self ):
    print( self.msg )

# Always do this so we can use this as a script or as a module
if __name__ == '__main__':

  # this call creates an object that is a new instance of the class
  object = HelloWorld()
  object.sayIt()
  # you could also do HelloWorld().sayIt()
  # this one actually calls HelloWorld.__str__() if it is defined
  print( object ); 
