#!/usr/bin/env python3
__author__ = "Sanjay Yellambalase Ravikumar"

def main():
    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    print_dict(animals)

def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')

"""
Methods:

    d = dict()
   
    d = dict(k1=v1, k2=v2, ...)
    d = {k1: v1, k2: v2, ...}

    d.items()
    d.keys()
    d.values()
    d[key]
    key in d
    d.get(key)


"""


if __name__ == '__main__': main()
