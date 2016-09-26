#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 10: Interactive vowels counter.
# Write a script that asks a user to enter an arbitrary string and returns
# a number of vowels in that string.
# Requirements and conditions:
# - use a built-in function raw_input();
# - use only latin letters;
# - vowels are 'a', 'e', 'i', 'o', 'u';
# - case-insensitive functionality.#
# EXAMPLE:
# Please, enter your string: wHAt Do yOU wANt fRom ME?
# The string contains 7 vowels
# Continue? (yes/no) maybe
# Please, enter correct answer. Continue? (yes/no) yes
# Hurray!
# Please, enter your string: HHHMMMMM...
# The string doesn't contain vowels
# Continue? (yes/no) no
# It was nice to count your vowels!

def count_vowels():
    inp = raw_input('Please, enter your string: ')
    count = 0
    for char in inp.lower():
        if char in 'aeiou':
            count += 1
    if count:
        print 'The string contains %s vowels' % count
    else:
        print "The string doesn't contain vowels"

def ask():
    mistake = 0
    while True:
        if not mistake:
            question = 'Continue? (yes/no) '
        else:
            question = 'Please, enter correct answer. Continue? (yes/no) '
        ans = raw_input(question)
        if ans == 'yes':
            mistake = 0
            print 'Hurray!'
            count_vowels()
            continue
        elif ans == 'no':
            mistake = 0
            print 'It was nice to count your vowels!'
            break
        else:
            mistake = 1

count_vowels()
ask()

