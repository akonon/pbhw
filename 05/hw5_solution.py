# -*- coding: utf-8 -*-

class Person(object):
    """Represents an entry in a contact list"""

    def __init__(self, surname, first_name, birth_date, nickname=None):
        from datetime import datetime

        self.surname = surname
        self.first_name = first_name
        self.birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
        if nickname:
            self.nickname = nickname

    def get_age(self):
        """Return person's age in years"""
        import datetime

        today = datetime.date.today()
        years_difference = today.year - self.birth_date.year
        is_before_birthday = (today.month, today.day) < (self.birth_date.month,
                                                         self.birth_date.day)
        age = years_difference - int(is_before_birthday)
        return str(age)

    def get_fullname(self):
        """Return person's full name"""
        return self.surname + ' ' + self.first_name
