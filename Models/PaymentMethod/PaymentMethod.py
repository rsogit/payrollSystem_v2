class PaymentMethod:

    def __init__(self, name, id=None, type=None):
        self._name = name
        self._id = id
        self._type = type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def id(self):
        return self._id
