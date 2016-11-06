#!/usr/env/bin python
# -*- coding: utf-8 -*-

u"""
Основной скрипт запуска ДЗ.

Данный скрипт призван запускать на выполнение домашнее задание #6.
"""


from hw6_solution import modifier


def runner():
    u"""Запускает выполнение всех задач"""
    print 'Modifying file...'
    modifier('data.csv')
    print 'Modified successfully!'


if __name__ == '__main__':
    runner()
