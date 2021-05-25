from Models.PaymentMethod.PaymentMethod import PaymentMethod


class Deposit(PaymentMethod):
    _account: int
    _agency: int

    def __init__(self, name="Depósito", id=None, type=None, agency=None, account=None):
        super().__init__(name, id, type)

        if agency and account:
            self._agency = agency
            self._account = account
        else:
            try:
                self._account = int(input("Digite apenas os números da conta bancária: "))
                self._agency = int(input("Digite apenas os números da agência bancária: "))
            except:
                print("Erro na entrada. Digite apenas os números da conta e agência. "
                      "Por favor tente novamente.")

    @property
    def agency(self):
        return self._agency

    @agency.setter
    def agency(self, agency):
        self._agency = agency

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, account):
        self._account = account
