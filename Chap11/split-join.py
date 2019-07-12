#!/usr/bin/env python3
__author__ = "Sanjay Yellambalase Ravikumar"

s = 'This is a long string with a bunch of words in it.'
print(s)

print(s.split())
print(s.split('i'))

l = s.split()
s2 = ':'.join(l)
print(s2)
