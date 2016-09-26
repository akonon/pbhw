#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 1: Squares.
# Take a sequence of numbers and return a sequence of the same type with squares
# of the numbers:
# [1, 2, 3] >> [1, 4, 9]
# (1, 2, 3) >> (1, 4, 9)
# set([1, 2, 3]) >> set([1, 4, 9])

def squares(t):
    return type(t)([i**2 for i in t])

# Test
if __name__ == '__main__':
    assert squares([1, 2, 3]) == [1, 4, 9]
    assert squares((1, 2, 3)) == (1, 4, 9)
    assert squares(set([1, 2, 3])) == set([1, 4, 9])
    print 'OK!'
