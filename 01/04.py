#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 4: The longest substring with letters in alphabetical order.
# s = "sabrrtuwacaddabra"
# ...
# >> "abrrtuw"

s = 'sabrrtuwacaddabra'

current = s[0]
longest = s[0]
for i in range(1, len(s)):
    if s[i] >= current[-1]:
        current += s[i]
        if len(current) > len(longest):
            longest = current
    else:
        current = s[i]
print longest
