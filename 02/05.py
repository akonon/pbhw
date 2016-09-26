#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 5: Separator.
# Take a list of any numbers and modify it as follows:
# - in the beginning of the list there should be odd numbers in ascending order;
# - followed by the even numbers in descending order.
# [1, 4, 8, 6, 3, 7, 1] >> [1, 1, 3, 7, 8, 6, 4]


def separator(t):
    new_t = sorted(t, reverse=True)
    for i, k in enumerate(new_t):
        if k%2 != 0:
            new_t.insert(0, new_t.pop(i))
    return new_t

# Test
if __name__ == '__main__':
    assert separator([1, 4, 8, 6, 3, 7, 1]) == [1, 1, 3, 7, 8, 6, 4]
    print 'OK!'
