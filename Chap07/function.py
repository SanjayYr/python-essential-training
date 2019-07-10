#!/usr/bin/env python3
__author__ = "Sanjay Yellambalase Ravikumar"

def main():
    kitten()

def kitten():
    print('Meow.')


def func2():
    num = 2
    print(f"func{num} called")

if __name__ == '__main__':
    main()
    func2()

"""

-   func2() or main() cannot be defined after if main check
    as python doesn't support forward declarations


"""


