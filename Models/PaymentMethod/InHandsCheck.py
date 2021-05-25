from Models.PaymentMethod.PaymentMethod import PaymentMethod


class InHandsCheck(PaymentMethod):

    def __init__(self, name="Cheque em mãos", id=None, type=None):
        super().__init__(name, id, type)