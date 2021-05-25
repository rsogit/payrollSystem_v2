from Models.Union.ServiceTaxes import ServiceTaxes


class UnionMember:
    _service_taxes: [ServiceTaxes]
    _monthly_tax: float
    _union_id: int

    def __init__(self, monthly_tax=None):
        if monthly_tax:
            self._monthly_tax = monthly_tax
        else:
            self._monthly_tax = 0.0
        self._is_active = False
        self._service_taxes = []

    @property
    def monthly_tax(self):
        return self._monthly_tax

    @monthly_tax.setter
    def monthly_tax(self, monthly_tax):
        self._monthly_tax = monthly_tax

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        self._is_active = is_active

    @property
    def service_taxes(self):
        return self._service_taxes

    @service_taxes.setter
    def service_taxes(self, service_taxes):
        self._service_taxes = service_taxes

    @property
    def union_id(self):
        return self._union_id

    @union_id.setter
    def union_id(self, union_id):
        self._union_id = union_id

    def add_service_fee(self):
        if self._is_active:
            tax = ServiceTaxes()
            if tax:
                self._service_taxes.append(tax)
            else:
                print("Falha na criacao da taxa. Por favor, tente novamente")
        else:
            print("Desculpe, mas o funcionário não é ativo no sindicato, ative-o nas opcoes de editar funcionário")
