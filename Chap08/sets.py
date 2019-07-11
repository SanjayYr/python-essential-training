#!/usr/bin/env python3
__author__ = "Sanjay Yellambalase Ravikumar"

def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a)
    print_set(b)

def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

"""
    
    s = set()
    sorted(s)
    
    item in s
    
    s1 - s2
    s1 | s2
    s1 ^ s2
    s1 & s2
    

    


"""

if __name__ == '__main__': main()
