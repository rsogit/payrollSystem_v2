from Models.Employee.Employee import Employee
from Models.Sale.Sale import Sale
from datetime import datetime


class Commissioned(Employee):
    _salary: float
    _percentage: float
    _sales: [Sale]

    def __init__(self, name, address, id_number, payment_method, salary=None, percentage=None, schedule_type="weekly 2 friday"):
        super().__init__(name, address, id_number, schedule_type, payment_method=payment_method)
        self._type = "Comissionado"
        self._sales = []
        if salary:
            self._salary = float(salary)
        else:
            self._salary = float(input("Informe o salário do funcionário: R$ "))
        if percentage:
            self._percentage = float(percentage) / 100
        else:
            self._percentage = float(input("Informe a porcentagem de comissão do funcionário (apenas números): ")) / 100

    def calculate_commission(self):
        total_sales: float = 0
        for sale in self.sales:
            total_sales = total_sales + sale.value
        commission = total_sales * self.percentage
        return commission

    def calculate_salary(self):
        commission = float(self.calculate_commission())
        tw_salary = self.salary / 2
        discounts = self.calculate_discounts()
        liquid_salary = tw_salary + commission - discounts
        self.pay_salary(brute_salary=tw_salary, liquid_salary=liquid_salary,commission=commission, union_discounts=discounts )

    def pay_salary(self, brute_salary, liquid_salary, commission, union_discounts):
        print("------------------------- Contracheque --------------------------\n")
        print("---------------------- Dados do Funcionário ---------------------\n")
        print(f'Nome: {self.name}')
        print(f'Endereço: {self.address}')
        print(f'Pagamento referente à: {self.schedule.pop(0).date()}')
        print("---------------------- Dados do pagamento -----------------------\n")
        print(f'Método de pagamento: {self.payment_method.name}')
        print(f'Salário Bruto: R$ {brute_salary}')
        print(f'Salário Líquido: R$ {liquid_salary}')
        print(f'Valor total de comissões: R$ {commission}')
        print(f'Total de descontos: R$ {union_discounts}')
        print()

        # Reseting non fixed values
        self._sales = []
        self.union_info.service_taxes = []
        self._last_pay_date = datetime.now()

    def add_sale(self):
        date = input("Insira a data da venda no formato DD/MM/AAAA. \nEx.: 08/04/2021\n")
        value = float(input("Digite o valor da venda: \nR$ "))
        sale_result = Sale(date, value)
        self._sales.append(sale_result)
        self.print_sales()

    def print_sales(self):
        for (index, sale) in enumerate(self._sales):
            print(f'{index+1} - Data da venda: {sale.date} - Valor: R$ {sale.value}')

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary >= 0:
            self._salary = salary
        else:
            print("O salário informado está incorreto.")

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        if percentage >= 0:
            self._percentage = percentage
        else:
            print("A porcentagem informada está incorreta.")

    @property
    def sales(self):
        return self._sales
