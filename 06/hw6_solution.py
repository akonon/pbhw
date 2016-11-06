# -*- coding: utf-8 -*-

import csv
import os

from hw5_solution import Person


def modifier(fname):
    """Add fullname and age columns to a CSV file."""

    fhand = open(fname, 'r')
    dictreader = csv.DictReader(fhand)
    fout = open('temp', 'w')
    columns = ['id', 'surname', 'name', 'fullname',
               'birthdate', 'nickname', 'age']
    writer = csv.DictWriter(fout, fieldnames=columns)
    writer.writeheader()
    for row in dictreader:
        surname = row['surname']
        first_name = row['name']
        birth_date = row['birthdate']
        nickname = row['nickname']
        person = Person(surname, first_name, birth_date, nickname)
        row['fullname'] = person.get_fullname()
        row['age'] = person.get_age()
        writer.writerow(row)
    fhand.close()
    fout.close()
    os.rename('temp', fname)
