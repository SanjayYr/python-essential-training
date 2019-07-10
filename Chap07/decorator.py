#!/usr/bin/env python3
__author__ = "Sanjay Yellambalase Ravikumar"

import time

def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1) * 1000} ms')
    return wrapper


@elapsed_time
def big_sum():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print(f'Big sum: {sum(num_list)}')

def main():
    big_sum()

def f1():
    print('this is f1')


x = f1

x()

def f1():
    def f2():
        print('this is f2')
    return f2

x = f1()  # f1 returns f2 and x is assigned f2
x()       # prints 'this is f2'. Here, f1 is a wrapper for f2.

if __name__ == '__main__': main()
