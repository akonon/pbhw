#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Main script for HW04.

Call functions and execute tests.
"""

import hw04
from hw04_tests import tests_for_hw04_1, tests_for_hw04_2


INPUT_1 = "AsBCda"
INPUT_2 = """Proin eget tortor risus. Cras ultricies ligula sed magna \
dictum porta. Donec rutrum congue leo eget malesuada."""


def runner():
    """Call all the functions"""
    print INPUT_1, ">>\n", hw04.relative_freq(INPUT_1)
    print INPUT_2, ">>\n", hw04.ellipsis(INPUT_2)
    print INPUT_2, ">>\n", hw04.ellipsis(INPUT_2, 10)
    print INPUT_2, ">>\n", hw04.ellipsis(INPUT_2, 15)


if __name__ == '__main__':
    runner()
    tests_for_hw04_1()
    tests_for_hw04_2()
