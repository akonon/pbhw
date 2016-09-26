#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 4: Odd-even.
# Take a list of any numbers and filter it:
# - remove odd numbers if the number of elements in the list is even;
# - remove even numbers if the number of elements in the list is odd.
# [3, 7, 12] >> [3, 7]
# [3, 7, 12, 7] >> [12]

def odd_even(t):
    if len(t)%2 != 0:
        new_t = [i for i in t if i%2 != 0]
    else:
        new_t = [i for i in t if i%2 == 0]
    return new_t


# Test
if __name__ == '__main__':
    assert odd_even([3, 7, 12]) == [3, 7]
    assert odd_even([3, 7, 12, 7]) == [12]
    print 'OK!'
