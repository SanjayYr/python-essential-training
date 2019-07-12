#!/usr/bin/env python3
__author__ = "Sanjay Yellambalase Ravikumar"

import sys, os

def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))

    v = sys.platform
    print(v)

    o_s = os.name
    print(o_s)
    
    path = os.getenv('PATH')
    print(path)
    
    cwd = os.getcwd()
    print(cwd)

"""
Modules:

    random
    datetime
    saytime


"""



if __name__ == '__main__': main()
