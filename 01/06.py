#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 6: А & B.
# Compare two objects which can be strings or integers.
# Depending on object's values return only one of the following messages:
# - "got a string" - if one of the objects is a string;
# - "bigger" - if А > В;
# - "equal" - if A == B;
# - "smaller" - if А < В.

def compare(a, b):
    if type(a) == str or type(b) == str:
        ans = 'got a string'
    elif a > b:
        ans = 'bigger'
    elif a == b:
        ans = 'equal'
    else:
        ans = 'smaller'
    return ans

print compare('abc', 'de')
print compare('abc', 123)
print compare(123, 'de')
print compare(1, 3)
print compare(5, 5)
print compare(3, 1)
