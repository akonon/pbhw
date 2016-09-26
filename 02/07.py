#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 7: Separator advanced (bonus)
# Do Task 5 with the additional condition:
# - do not return a new list, modify the existing list you pass as an argument.
# start_list = [1, 4, 8, 6, 3, 7, 1]
# end_list = separator_advanced(start_list)
# start_list is end_list == True

def separator_advanced(t):
    t.sort(reverse=True)
    for i in range(len(t)):
        if t[i]%2 != 0:
            t.insert(0, t.pop(i))
    return t

# Test
if __name__ == '__main__':
    start_list = [1, 4, 8, 6, 3, 7, 1]
    end_list = separator_advanced(start_list)
    assert start_list is end_list
    print 'OK!'




