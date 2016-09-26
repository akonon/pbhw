#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 8: Every third element.
# Take a tuple of elements and return a tuple of every third element.
# Solve the task in two different ways.
# t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c')
# ...
# >> (3, 6, 9, 'b')

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c')

# way 1
print t[2::3]

# way 2
new_t = []
for i in range(len(t)):
    if (i+1)%3 == 0:
        new_t.append(t[i])
new_t = tuple(new_t)
print new_t
