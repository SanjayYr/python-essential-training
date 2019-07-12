#!/usr/bin/env python3
__author__ = "Sanjay Yellambalase Ravikumar"

class Bunny:
    def __init__(self, n):
        self._n = n
        
    def __repr__(self):
        return f'the number of bunnies is {self._n}'
    
    def __str__(self):
        return f'str: the number of bunnies is {self._n}'


s = Bunny(43)

# repr and ascii are similar
print(repr(s))
print(ascii(s))


# returns __str__ method output
# this return repr version if str is not overriden
print(s)

"""

chr() - unicode value to symbol
ord() - symbol to unicode value


"""

x = (1,2,3,4,5)
yr = reversed(x)
yl = list(x)
ys = sorted(x)

ysum = sum(x)
ymx = max(x)
ymn = min(x)
ya = any(x)
yall = all(x)

print(x)
print(yr)
print(yl)
print(ys)
print(ysum)
print(ymx)
print(ymn)
print(ya)
print(yall)

x2 = (6,7,8,9,10)

yz = zip(x,x2)

for a,b in yz: print(f'{a}-{b}')

x3 = ('cat', 'dog', 'bird', 'whale')

for i,v in enumerate(x3): print(f'{i}: {v}')

x4 = 42
zt = type(x)
xi = isinstance(x4, int)
xid = id(x)


