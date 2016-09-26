#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 9: XYZ.
# Don't use any conditional statements. Use only the built-in min() and max()
# functions. Take three numbers X, Y, Z and return one in the following order:
# - X, if Y < X;
# - Z, if Y > Z;
# - Y, otherwise

def cut(x, y, z):
    return max(x, min(z, y))

#         X  Y  Z
print cut(2, 1, 3)  # 2
print cut(1, 3, 2)  # 2
print cut(1, 2, 3)  # 2
