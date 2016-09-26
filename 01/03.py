#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 3: Count occurences of a substring.
# Count overlapping occurenses as well.
# s = "wowhatamanwowowpalehche"
# ...
# print count  # 3

s = 'wowhatamanwowowpalehche'

count = 0
for i in range(len(s)):
    if s[i:i+3] == 'wow':
        count += 1
print count
