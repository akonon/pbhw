#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 2: Symmetry.
# Take a string and check if it's symmetrical.
# "abba" >> True
# "arbat" >> False

def is_symmetric(s):
    if not s or len(s) % 2 != 0:
        return False
    # Recursive helper function
    def check(s):
        if len(s) == 2 and s[0] == s[-1]:
            return True
        else:
            return check(s[1:-1])
    return check(s)


# Test
if __name__ == '__main__':
    assert is_symmetric('abba') == True
    assert is_symmetric('arbat') == False
    print 'OK!'
