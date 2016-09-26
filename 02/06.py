#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 6: Classifier. (bonus)
# Take a dict with values of different type, return a dict of type:
# {value_type: number_of_elements_of_that_type}.
# {'a': 1, 3: [1,5], 'e': 'abc', '6': []} >> {'str': 1, 'list': 2, 'int': 1}

def classificator(d):
    counts = dict()
    for val in d.values():
        key = type(val).__name__
        counts[key] = counts.get(key, 0) + 1
    return counts


# Test
if __name__ == '__main__':
    assert classificator({'a': 1, 3: [1,5], 'e': 'abc', '6': []}) == \
                         {'str': 1, 'list': 2, 'int': 1}
    print 'OK!'
