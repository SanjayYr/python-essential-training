#!/usr/bin/env python3

__author__ = "Sanjay Yellambalase Ravikumar"

import platform

def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))

if __name__ == '__main__': main()
