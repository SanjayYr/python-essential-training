#!/usr/bin/env python3
__author__ = "Sanjay Yellambalase Ravikumar"

def main():
    f = open('lines.txt')
    """

    f = open('lines.txt', 'r')
    f = open('lines.txt', 'w')
    f = open('lines.txt', 'a')
    f = open('lines.txt', 'r+t')
    f = open('lines.txt', 'r+b')

    """
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()
