#!/usr/bin/env python3
__author__ = "Sanjay Yellambalase Ravikumar"

x = 0x0a
y = 0x02

z = x & y
z = x | y
z = x ^ y
z = x << y
z = x >> y



print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
