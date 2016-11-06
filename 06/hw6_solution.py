# -*- coding: utf-8 -*-

class Person(object):
    """Represents an entry in a contact list"""

    def __init__(self, csvdict):
        """Take a dictionary 'column_name': 'value'"""
        from datetime import datetime

        self.surname = csvdict['surname']
        self.name = csvdict['name']
        self.birthdate = datetime.strptime(csvdict['birthdate'],
                                           '%Y-%m-%d').date()
        self.nickname = csvdict['nickname']

    def get_age(self):
        """Return person's age in years"""
        import datetime

        today = datetime.date.today()
        years_difference = today.year - self.birthdate.year
        is_before_birthday = (today.month, today.day) < (self.birthdate.month,
                                                         self.birthdate.day)
        age = years_difference - int(is_before_birthday)
        return str(age)

    def get_fullname(self):
        """Return person's full name"""
        return self.surname + ' ' + self.name


def modifier(fname):
    """Add fullname and age columns to CSV data in a file."""
    import csv, os

    fhand = open(fname, 'rb')
    dictreader = csv.DictReader(fhand)
    fout = open('new_'+fname, 'wb')
    writer = csv.writer(fout)
    columns = ['id', 'surname', 'name', 'fullname',
               'birthdate', 'nickname', 'age']
    writer.writerow(columns)
    for row in dictreader:
        person = Person(row)
        new_row = [row['id'], row['surname'], row['name'],
                   person.get_fullname(), row['birthdate'],
                   row['nickname'], person.get_age()]
        writer.writerow(new_row)
    fhand.close()
    fout.close()
    os.rename('new_'+fname, fname)
