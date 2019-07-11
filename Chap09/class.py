#!/usr/bin/env python3
__author__ = "Sanjay Yellambalase Ravikumar"

class Duck:
    # data
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

    # methods
    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)

def main():
    donald = Duck()
    donald.quack()
    donald.move()

if __name__ == '__main__': main()
