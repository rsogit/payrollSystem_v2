from Models.Employee.Employee import Employee
from datetime import datetime


class Salaried(Employee):
    _salary: float

    def __init__(self, name, address, id_number, payment_method, salary=None, schedule_type="monthly $"):
        super().__init__(name, address, id_number, schedule_type, payment_method=payment_method)
        self._type = "Assalariado"
        if salary:
            self._salary = float(salary)
        else:
            self._salary = float(input("Informe o salário do funcionário: R$ "))

    def calculate_salary(self):
        discounts = float(self.calculate_discounts())
        liquid_salary = self.salary - discounts
        self.pay_salary(self.salary, liquid_salary, discounts)

    def pay_salary(self, brute_salary, liquid_salary, union_discounts):
        print("------------------------- Contracheque --------------------------\n")
        print("---------------------- Dados do Funcionário ---------------------\n")
        print(f'Nome: {self.name}')
        print(f'Endereço: {self.address}')
        print(f'Pagamento referente à: {self.schedule.pop(0).date()}')
        print("---------------------- Dados do pagamento -----------------------\n")
        print(f'Método de pagamento: {self.payment_method.name}')
        print(f'Salário Bruto: R$ {brute_salary}')
        print(f'Salário Líquido: R$ {liquid_salary}')
        print(f'Total de descontos: R$ {union_discounts}')
        print()

        # Reseting non fixed values
        self.union_info.service_taxes = []
        self._last_pay_date = datetime.now()

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary >= 0:
            self._salary = salary
        else:
            print("O salário informado está incorreto.")