from Models.PaymentMethod.PaymentMethod import PaymentMethod


class MailCheck(PaymentMethod):
    _address: str

    def __init__(self, address: str="Endereco genérico", name="Cheque via Correios", id=None, type=None):
        super().__init__(name, id, type)
        self._address = address

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address
