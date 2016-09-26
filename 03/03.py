# -*- coding: utf-8 -*-

# Task 1: Vowels again.
# Count a number of vowels in each word of the given string.
# Return the max number of vowels in a single word.
# Text:
# Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.
# Vowels: A, E, I, O, U

def vowels_counter(s):
    """Count vowels in words and return max number of vowels in single word."""
    t = set([])
    words = s.lower().split()
    for word in words:
        count = 0
        for char in word:
            if char in 'aeiou':
                count += 1
        t.add(count)
    return max(t)




# ==============================================================================
# Task 2: The longest word
# Return the longest word in text. If there are many words - return a list.
# Text:
# Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada.

def longest_words(s):
    """Find the longest words in a string s and return a list."""
    import string

    s = s.lower().translate(None, string.punctuation)
    counts = {word: len(word) for word in s.split()}
    words = sorted(k for k, v in counts.items() if v == max(counts.values()))

    return words


# ==============================================================================
# Task 3: Reserse'em!
# Take some text and reverse the order of:
# - letters in words;
# - words in sentences;
# - sentences in text.
# Return the reversed text.
# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. Cras ultricies ligula sed magna dictum porta.

def reverse_em(s):
    """Reverse letters in words, words in sentences, sentences in text."""
    return s[::-1]

# ==============================================================================
# Task 4: Imports.
# Import standard Python libraries "os" and "sys".
# Print out documentation about functions of both libraries.
import os
import sys

# print os.__doc__
# print sys.__doc__


# ==============================================================================
# Task 5: Pseudosum.
# Take a positive integer.
# Return a sum of digits the input number consists of.
# Don't use the '+' operator and the built-in function sum().
# 456 >> 15

def pseudo_sum(num):
    """Break an integer into separate digits and return their sum."""
    result = 0
    for char in str(num):
        result -= int(char)
    return -result

def pseudo_sum_list(num):
    """Break an integer into separate digits and return their sum."""
    t = []
    for i in str(num):
        t.extend(range(int(i)))
    return len(t)

# ==============================================================================
# Task 6: Prime numbers. (bonus)
# Print out the first 10000 natural prime numbers.

def prime_finder(n):
    """Generate the first n prime numbers starting from 2."""
    if n >= 1:
        yield 2
        n -= 1
    num = 3
    while n > 0:
        for i in range(2, int(num**0.5) + 1):
            if num%i == 0:
                break
        else:
            yield num
            n -= 1
        num += 2


# ==============================================================================
# Task 7: Reverse'em all! (bonus)
# Do Task 3 but save positions of:
# - punctuation marks ("word," >> "drow,");
# - Capital letters at the beginning of the sentences ("Word ..." >> "Drow ...")

def reverse_em_advanced(s):
    """Reverse letters in words, words in sentences, sentences in text.

    Save positions of commas ("word," >> "drow,") and capital letters
    ("Word ..." >> "Drow ...").
    """
    text = []
    sentences = s.strip('.').split('.')
    for sentence in sentences:
        words = []
        for word in sentence.split():
            sign = ''
            if not word[-1].isalpha():
                word, sign = word[:-1], word[-1]
            if word.istitle():
                word = word[:-1].lower() + word[-1].upper()
            words.append(word[::-1] + sign)
        words.reverse()
        text.append(' '.join(words))
    text.reverse()
    new_text = '.' + ' .'.join(text)
    return new_text


# ==============================================================================
# Task 8: A-a-a (bonus)
# Count "a"s in text only if they are surrounded by consonants ("car").
# Text:
# Cras ultricies ligula sed magna dictum porta. Vivamus magna justo, lacinia eget consectetur sed, convallis at tellus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec velit neque, auctor sit amet aliquam vel, ullamcorper sit amet ligula. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur aliquet quam id dui posuere blandit. Quisque velit nisi, pretium ut lacinia in, elementum id enim. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed porttitor lectus nibh.
# Consonants: all letters except A, E, I, O, U
# ==============================================================================

def a_counter_re(s):
    """Count all 'a's if they are surrounded by consonants. Ex: 'car'."""
    import re
    pattern = '[bcdfghjklmnpqrstvwxyz]a[bcdfghjklmnpqrstvwxyz]'
    x = re.findall(pattern, s.lower())
    return len(x)

def a_counter(s):
    """Count all 'a's if they are surrounded by consonants. Ex: 'car'."""
    consonants = 'bcdfghjklmnpqrstvwxyz'
    words = s.lower().split()
    count = 0
    for word in words:
        for i in range(len(word)-2):
            if word[i] in consonants and word[i+1] == 'a' and \
                    word[i+2] in consonants:
                count += 1
    return count


# Tests
if __name__ == '__main__':
    # 1
    text = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada."
    assert vowels_counter(text) == 5
    print '1 - OK!'

    # 2
    text = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada."
    assert longest_words(text) == ['convallis', 'curabitur', 'malesuada', 'ultricies']
    print '2 - OK!'

    # 3
    text = "Lorem ipsum dolor, consectetur elit. Nulla quis feugiat. Donec leo eget malesuada. Cras ultricies porta."
    rev_text = ".atrop seicirtlu sarC .adauselam tege oel cenoD .taiguef siuq alluN .tile rutetcesnoc ,rolod muspi meroL"
    assert reverse_em(text) == rev_text
    print '3 - OK!'

    # 4
    print '4 - OK!'

    # 5
    assert pseudo_sum(456) == 15
    print '5 - OK!'

    # 6
    for i in prime_finder(10000): pass
    assert i == 104729
    print '6 - OK!'

    # 7
    text = "Lorem ipsum dolor, consectetur elit. Nulla quis feugiat. Donec leo eget malesuada. Cras ultricies porta."
    rev_text = ".atrop seicirtlu Sarc .adauselam tege oel Cenod .taiguef siuq Allun .tile rutetcesnoc rolod, muspi Merol"
    assert reverse_em_advanced(text) == rev_text
    print '7 - OK!'

    # 8
    text = "Cras ultricies ligula sed magna dictum porta. Vivamus magna justo, lacinia eget consectetur sed, convallis at tellus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec velit neque, auctor sit amet aliquam vel, ullamcorper sit amet ligula. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur aliquet quam id dui posuere blandit. Quisque velit nisi, pretium ut lacinia in, elementum id enim. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed porttitor lectus nibh."
    assert a_counter_re(text) == 10
    assert a_counter(text) == 10
    print '8 - OK!'
