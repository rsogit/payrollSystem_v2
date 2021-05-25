from Models.Union.UnionMember import UnionMember
import pandas as pd
from datetime import datetime
from datetime import date
from Utils.Utils import get_week_day

from Models.PaymentMethod.PaymentMethod import PaymentMethod


class Employee:
    _type: str
    _union_info: UnionMember
    _last_pay_date: date
    _schedule_type: str
    _schedule: [date] = []
    _payment_method: PaymentMethod

    def __init__(self, name, address, id_number, schedule_type, payment_method):
        self._name = name
        self._address = address
        self._id_number = id_number
        self._schedule_type = schedule_type
        self._last_pay_date = datetime.now().date()
        self._union_info = UnionMember()
        self._payment_method = payment_method
        self.set_schedule(schedule_type)

    def set_schedule(self, schedule_type: str):
        schedule_types = schedule_type.split(" ")
        hour = self._last_pay_date
        first_frequency = schedule_types[0]
        try:
            day_frequency = int(schedule_types[1])
        except:
            day_frequency = schedule_types[1]
        if len(schedule_types) < 3:
            weekday_frequency = "monday"
        else:
            weekday_frequency = schedule_types[2]

        # Caso a frequência seja mensal, gera o intervalo com o offset do dia n.
        # Caso o dia seja "$", gera o intervalo com o offset para o último dia útil
        if first_frequency == "monthly" or first_frequency == "mensal":
            if isinstance(day_frequency, int):
                if 0 < day_frequency <= 31:
                    range = pd.date_range(hour, periods=12, freq='MS') \
                            + pd.DateOffset(days=(day_frequency-1))
                    self._schedule = range.tolist()
                else:
                    print("Selecione um dia do mês válido")
            elif day_frequency == "$":
                range = pd.date_range(hour, periods=12, freq='BM')
                self._schedule = range.tolist()
            else:
                print("A expressão de agenda de pagamento customizado está inválida, "
                      "tente novamente no formato 'weekly 2 friday', por exemplo")

        # Caso a frequência seja semanal, gera o intervalo com o offset no dia da semana.
        elif first_frequency == "weekly" or first_frequency == "semanal":
            if weekday_frequency:
                if isinstance(day_frequency, int):
                    range = pd.date_range(hour, periods=12, freq=f'{day_frequency}W-{get_week_day(weekday_frequency)}')
                    self._schedule = range.tolist()
            else:
                print("A expressão de agenda de pagamento customizado está inválida, "
                      "tente novamente no formato 'weekly 2 friday', por exemplo")
        else:
            return []

    def calculate_discounts(self):
        total_service_fee = 0
        if self.union_info.is_active:
            if len(self.union_info.service_taxes) > 0:
                for service_fee in self.union_info.service_taxes:
                    total_service_fee = total_service_fee + service_fee.value
        return total_service_fee + self.union_info.monthly_tax

    @property
    def schedule_type(self):
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        self._schedule_type = schedule_type

    @property
    def schedule(self):
        return self._schedule

    @schedule.setter
    def schedule_type(self, schedule):
        self._schedule = schedule

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def id_number(self):
        return self._id_number

    @property
    def union_info(self):
        return self._union_info

    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        self._payment_method = payment_method
