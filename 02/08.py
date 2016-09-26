#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 8: Pairs. (bonus)
# Take a one-level tuple and turn it into a tuple of pairs:
# (1, 4, 8, 6, 3, 7, 1) >> ((1, 4), (8, 6), (3, 7), (1,))

def two_level_tuple(t):
    new_t = []
    for i in range(0, len(t), 2):
        try:
            new_t.append((t[i], t[i+1]))
        except IndexError:
            new_t.append((t[i],))
    return tuple(new_t)


# Test
if __name__ == '__main__':
    assert two_level_tuple((1, 4, 8, 6, 3, 7, 1)) == ((1, 4),(8, 6),(3, 7),(1,))
    assert two_level_tuple((1,)) == ((1,),)
    print 'OK!'
