#!/usr/bin/env python3

a = 3
b = 2

# lets check they are both non-negative numbers
if a < 0 or b < 0:
    print("at least one is negative!")
    exit

# lets check that a is in a certain range
if a > 2 and a <= 4:
    print("a satisfies this range (2, 4]")
