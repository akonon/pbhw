#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 2: count vowels.
# Vowels are 'a', 'e', 'i', 'o' and 'u'.
# s = "hApPyHalLOweEn!"
# ...
# print count  # 5

s = 'hApPyHalLOweEn!'

count = 0
for char in s.lower():
    if char in 'aeiou':
        count += 1
print count
