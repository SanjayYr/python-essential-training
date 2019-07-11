#!/usr/bin/env python3
__author__ = "Sanjay Yellambalase Ravikumar"

import sys

def main():
    try:
        #x = int('foo')
        x = 5/0
    except ValueError:
        print('ValueError caught')
    except:
        print(f'Unknown error: {sys.exc_info()}')

if __name__ == '__main__': main()
