#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 9: Flattening. (bonus)
# Take a list of lists and flatten it:
# [[1], [4, 8], [6, 3, 7], [1, 3]] >> [1, 4, 8, 6, 3, 7, 1, 3]

def flatten(t):
    return [num for lst in t for num in lst]


# Test
if __name__ == '__main__':
    assert flatten([[1], [4, 8], [6, 3, 7], [1, 3]]) == [1, 4, 8, 6, 3, 7, 1, 3]
    print 'OK!'

