#!/usr/bin/env python3
__author__ = "Sanjay Yellambalase Ravikumar"

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    print_list(game)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

"""
Methods:

    l = list()
    l.index(item)
    l.append(item)
    l[i]
    l.insert(i, item)
    l.remove(item)
    l.pop()
    l.pop(i)
    del l[i]
    del l
    ', '.join(l)
    len(l)

    sorted(l)

"""

if __name__ == '__main__': main()
