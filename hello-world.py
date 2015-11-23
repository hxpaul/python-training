#!/usr/bin/env python3

# There are 5 or 6 of these __future__ imports to worry about
# it does nothing in python3 but means our code
# will run in python2 as well
from __future__ import print_function

print('Hello','world', '\n')

data = ['hello', 'world'] # mutable sequence
print( data ) # displays that array best it can
print( data[0] + ' ' + data[1] ) # 'hello world'
print( data[0], data[1] ) # 'hello world'

# if you don't need to change the values, enforce this by making it imdata
data = ('hello', 'world')
print( data ) # displays that tuple best it can
print( data[0] + ' ' + data[1] ) # 'hello world'
print( data[0], data[1] ) # 'hello world'

print( len( data ), 'items in immutable sequence' );

# everything is done with indenting

# this is not pythonic, don't use "while" when we have a bounded range
i = 0
while i < len( data ):
  print( data[i] )
  i += 1

# this is more pythonic, use the range
for i in range( len( data )):
  print( data[i] )

# this is even more pythonic, we don't need the index in this case
for val in data:
  print( val )

print( ' '.join( data ))

# dictionary / hash / map works like a sequence, as in js
# these two are the same
# { 0: 'hello', 1: 'world' }
# [ 'hello', 'world' ]
data = { 'foo': 'bar', 'baz': 'etc' }
print( data['foo'], data['baz'] )
