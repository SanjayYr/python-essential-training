#!/usr/bin/env python3
__author__ = "Sanjay Yellambalase Ravikumar"

def main():
    kitten(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')
    
    print('\nRepeat function call\n')
    
    # notice 2 asteriks

    x = dict(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')
    kitten(**x)

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('Meow.')

if __name__ == '__main__': main()
