# -*- coding: utf8 -*-

"""
Tests for HW04
"""

import hw04


def tests_for_hw04_1():
    """Tests for Task 1"""
    assert hw04.relative_freq("A") == {'a': 100.0}
    assert hw04.relative_freq("ABCda") == {
        'a': 40.0, 'b': 20.0, 'c': 20.0, 'd': 20.0
    }
    assert hw04.relative_freq("AsBCda") == {
        'a': 33.3, 'b': 16.7, 'c': 16.7, 'd': 16.7, 's': 16.7
    }
    assert hw04.relative_freq("q TyU#!{}.") == {
        'q': 25.0, 't': 25.0, 'y': 25.0, 'u': 25.0
    }
    assert sum(hw04.relative_freq("q TyU#!{}.").values()) == 100.0
    print 'Tests 1 - OK!'


def tests_for_hw04_2():
    """Tests for Task 2"""
    text = "Proin eget tortor risus."
    assert hw04.ellipsis(text) == "Proin eget tortor risus."
    assert hw04.ellipsis(text, 24) == "Proin eget tortor risus."
    assert hw04.ellipsis(text, 23) == "Proin eget tortor..."
    assert hw04.ellipsis(text, 13) == "Proin eget..."
    assert hw04.ellipsis(text, 6) == "Pro..."
    print 'Tests 2 - OK!'
