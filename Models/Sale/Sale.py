class Sale:

    def __init__(self, date, value):
        self._date = date
        self._value = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value