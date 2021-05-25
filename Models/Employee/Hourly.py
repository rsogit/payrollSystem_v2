from Models.Employee.Employee import Employee
from Models.TimeCard.TimeCard import TimeCard
from datetime import datetime


class Hourly(Employee):
    _hourly_salary: float
    _time_cards: [TimeCard]

    def __init__(self, name, address, id_number, payment_method, hourly_salary=None, schedule_type="weekly 1 friday"):
        super().__init__(name, address, id_number, schedule_type, payment_method=payment_method)
        self._type = "Horista"
        self._time_cards = []
        if hourly_salary:
            self._hourly_salary = hourly_salary
        else:
            self._hourly_salary = float(input("Informe a hora de trabalho do funcionário: R$ "))

    def calculate_salary(self):
        max_hours = 8
        total_hours = 0
        brute_salary = 0
        for timecard in self._time_cards:
            day_hours = timecard.work_hours.seconds / 3600
            if day_hours > max_hours:
                bonus_hours = (day_hours - max_hours)
                bonus_salary = bonus_hours * self._hourly_salary * 1.5
                total_hours = total_hours + day_hours
                brute_salary = total_hours * self._hourly_salary + bonus_salary
            else:
                total_hours = total_hours + day_hours
                brute_salary = total_hours * self._hourly_salary
        discounts = float(self.calculate_discounts())
        liquid_salary = brute_salary - discounts
        self.pay_salary(brute_salary, liquid_salary, total_hours, discounts)

    def pay_salary(self, brute_salary, liquid_salary, worked_hours, union_discounts):
        print("-----------------------------------------------------------------\n")
        print("------------------------- Contracheque --------------------------\n")
        print("---------------------- Dados do Funcionário ---------------------\n")
        print(f'Nome: {self.name}')
        print(f'Endereço: {self.address}')
        print(f'Pagamento referente à: {self.schedule.pop(0).date()}')
        print("---------------------- Dados do pagamento -----------------------\n")
        print(f'Método de pagamento: {self.payment_method.name}')
        print(f'Horas trabalhadas no período: {worked_hours}')
        print(f'Salário Bruto: R$ {brute_salary}')
        print(f'Salário Líquido: R$ {liquid_salary}')
        print(f'Total de descontos: R$ {union_discounts}')
        print("-----------------------------------------------------------------\n")

        # Reseting non fixed values
        self.time_cards = []
        self.union_info.service_taxes = []
        self._last_pay_date = datetime.now()

    def add_timecard(self):
        fmt = "%H:%M"
        time_in = input("Digite o horário de entrada no formato HH:MM. \nEx.: '08:00'\n")
        date_time_in = datetime.strptime(time_in, fmt)
        time_out = input("Digite o horário de saída no formato HH:MM. \nEx.: '12:00'\n")
        date_time_out = datetime.strptime(time_out, fmt)

        if date_time_out >= date_time_in:
            work_hours = date_time_out - date_time_in
            timecard = TimeCard(date_time_in.time(), date_time_out.time(), work_hours)
            self._time_cards.append(timecard)
        else:
            print("O horário informado é inválido. Por favor, preencha o horário de entrada e saída na ordem correta.")


    def print_timecards(self):
        for (index, time_card) in enumerate(self._time_cards):
            print(f'{index+1} - Horas trabalhadas: {time_card.work_hours}hrs')

    @property
    def time_cards(self):
        return self._time_cards

    @time_cards.setter
    def time_cards(self, time_cards):
        self._time_cards = time_cards

    @property
    def hourly_salary(self):
        return self._hourly_salary

    @hourly_salary.setter
    def hourly_salary(self, hourly_salary):
        self._hourly_salary = hourly_salary
