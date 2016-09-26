#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 1: Reverse.
# Reverse a string "ecnalubma" in four different ways:
# "ecnalubma" >> "ambulance"

a = 'ecnalubma'

# way 1
result = a[::-1]
print result

# way 2
result = ''
for char in a:
    result = char + result
print result

# way 3
result = list(a)
result.reverse()
result = ''.join(result)
print result

# way 4
result = ''
for char in reversed(a):
    result += char
print result

# way 5
result = ''
index = -1
while index >= -len(a):
    result += a[index]
    index -= 1
print result
