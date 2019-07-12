#!/usr/bin/env python3
__author__ = "Sanjay Yellambalase Ravikumar"

print('Hello, World.'.upper())
print('Hello, World.'.swapcase())
print('Hello, World.'.capitalize())
print('Hello, World.'.title())
print('Hello, World.'.casefold())

s = 'Hello {}'
print(s.format(42*8))

s = 'first string ' 'second string'
print(s)

x = 43*1992
print('the number is {:,}'.format(x))
print('the number is {:.3f}'.format(x))
print('the number in hex is {:x}'.format(x))
print('the number in octal is {:o}'.format(x))
print('the number in binary is {:b}'.format(x))
