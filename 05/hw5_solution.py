# -*- coding: utf-8 -*-

class Person(object):
    """Represents an entry in a contact list"""

    def __init__(self, surname, first_name, birth_date, nickname=None):
        self.surname = surname
        self.first_name = first_name
        self.birth_date = birth_date
        self.nickname = nickname

    def get_age(self):
        """Calc person's age and return a full number of years"""

    def get_fullname(self):
        """Get person's full name: 'surname firstname'"""
        return self.surname + ' ' + self.first_name
