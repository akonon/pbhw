#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 3: Trichotomy.
# Take a list of ints and return a dict: {int: boolean}
# where boolean is True or False depending on
# if the integer is divisible by 3 withour remainder.
# [3,7,12] >> {3: True, 12: True, 7: False}

def tridivision(t):
    d = dict()
    for i in t:
        d[i] = (i%3 == 0)
    return d

# Test
if __name__ == '__main__':
    assert tridivision([3, 7, 12]) == {3: True, 12: True, 7: False}
    print 'OK!'
