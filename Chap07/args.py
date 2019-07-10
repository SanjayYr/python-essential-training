#!/usr/bin/env python3
__author__ = "Sanjay Yellambalase Ravikumar"

def main():
    kitten('meow', 'grrr', 'purr')

    print('\nRepeat function call\n')
    # below works the same as calling above
    x = ('meow', 'grrr', 'purr')
    kitten(*x)


def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else: print('Meow.')

if __name__ == '__main__': main()
