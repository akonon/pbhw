# -*- coding: utf-8 -*-

# Task 1: Relative frequencies of letters
# Count relative weights of letters in a string (in percent). Case-insensitive.
# Print out a dictionary:
# {letter: its_percentage_of_occurence_in_the_string}
# Round values to the first decimal place.
# Example:
# 'ABCda' >> {'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0}

def relative_freq(text):
    """Find relative frequencies of letters and return a dict {letter: %}"""
    import string

    counts = dict()
    for char in text.lower():
        if char in string.lowercase:
            counts[char] = counts.get(char, 0) + 1

    total = float(sum(counts.values()))
    for char, count in counts.items():
        counts[char] = round((count/total)*100, 1)

    return counts



# Task 2: Epsilon...
# Cut a string and add '...' to the end.
# Take two arguments:
# - a string
# - a limit (optional, default=0), desired length of the string after cutting.
# Cut the string according to the limit, but keep in mind that:
# - words should not but cut in the middle (except the first one);
# - the lenght of the resulting string (including '...') should be equal to the
#   limit (if given).#  
# Examples:
# text = "Proin eget tortor risus."
# limit = 24
# output = "Proin eget tortor risus."
# limit = 23
# output = "Proin eget tortor..."
# limit = 13
# output = "Proin eget..."
# limit = 6
# output = "Pro..."

def ellipsis(text, limit=0):
    """Shorten text and add ellipsis (...) at the end."""
    assert limit == 0 or limit >= 3, 'Invalid limit argument!'

    if not limit or limit >= len(text):
        return text

    cut_text = text[:limit-2]
    space_pos = cut_text[::-1].find(' ')
    if space_pos <= 0:
        return cut_text[:-1] + '...'
    return cut_text[:-space_pos-1] + '...'

