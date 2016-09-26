#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 7: Deduplication.
# Take a list of elements and remove all duplicates in two ways:
# - save the original order of the elements in the resulting list;
# - the resulting list shoud with new random order of the elements.
# ["a", 5, 2, 5, (1, "a"), "a"] >> ["a", 5, 2, (1, "a")]
# ["a", 5, 2, 5, (1, "a"), "a"] >> [2, "a", 5, (1, "a")]

def unique_ordered(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst

def unique_disordered(lst):
    return list(set(lst))

t = ["a", 5, 2, 5, (1, "a"), "a"]

print unique_ordered(t)      # ["a", 5, 2, (1, "a")]
print unique_disordered(t)   # [2, "a", 5, (1, "a")]
