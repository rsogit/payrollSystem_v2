from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime


class MainMenuStrategy(ABC):

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def show_menu_option(self, employees) -> None:
        self._strategy.show_menu_option(employees)


class Strategy:

    @abstractmethod
    def show_menu_option(self, employees):
        pass


class AddEmployeeMenuStrategy(Strategy):

    def show_menu_option(self, company):
        company.add_employee()


class ListEmployeeMenuStrategy(Strategy):

    def show_menu_option(self, company):
        if len(company.employees) != 0:
            company.show_employees(company.employees)
        else:
            print("Não há funcionários cadastrados")


class EditEmployeeMenuStrategy(Strategy):

    def show_menu_option(self, company):
        print("Digite o ID do funcionário que deseja editar: ")
        company.show_employees(company.employees)
        employee_number = int(input("\n"))
        company.edit_employee(len(company.employees), employee_number)


class RemoveEmployeeMenuStrategy(Strategy):

    def show_menu_option(self, company):
        print("Digite o ID do funcionário que deseja deletar: ")
        company.show_employees(company.employees)
        employee_number = int(input("\n"))
        company.delete_employee(len(company.employees), employee_number)


class AddTimeCardMenuStrategy(Strategy):

    def show_menu_option(self, company):
        print("Digite o ID do funcionário que deseja adicionar o Cartão de Ponto:\n")
        company.show_employees(company.employees, "Horista")
        option = int(input(""))
        selected_employee = [x for x in company.employees if x.id_number == option].pop()
        selected_employee.add_timecard()


class AddSaleResultMenuStrategy(Strategy):

    def show_menu_option(self, company):
        print("Digite o ID do funcionário que deseja adicionar o Resultado de Venda:\n")
        company.show_employees(company.employees, "Comissionado")
        option = int(input(""))
        selected_employee = [x for x in company.employees if x.id_number == option].pop()
        selected_employee.add_sale()


class AddServiceFeeMenuStrategy(Strategy):

    def show_menu_option(self, company):
        print("Digite o ID do funcionário que deseja adicionar a Taxa de Servico Sindical:\n")
        union_employees = [x for x in company.employees if x.union_info.is_active]
        if len(union_employees) > 0:
            company.show_union_employees(union_employees)
            option = int(input(""))
            selected_employee = [x for x in company.employees if x.id_number == option].pop()
            selected_employee.union_info.add_service_fee()
        else:
            print("Não há funcionários ativos no sindicato")


class RunPayrollMenuStrategy(Strategy):

    def show_menu_option(self, company):
        print("Deseja rodar a folha de pagamento para hoje ou outro dia?\n"
              "1 - Rodar para hoje\n"
              "2 - Rodar para outra data")
        opt = int(input())
        if opt == 1:
            company.run_payroll(company.employees)
        elif opt == 2:
            fmt = "%d/%m/%Y"
            try:
                run_date = input("Digite a data que deseja rodar a folha de pagamento, "
                                                   "no formato DD/MM/AAAA: ")
                run_date = datetime.strptime(run_date, fmt)
            except:
                print("Data inválida, rodando folha de pagamento para hoje: ")
                run_date = datetime.now()
            company.get_payroll(company.employees, run_date)


class AddScheduleMenuStrategy(Strategy):

    def show_menu_option(self, company):
        new_schedule = input("Por favor digite a nova agenda de pagamentos que deseja adicionar, "
                             "como no exemplo 'weekly 3 monday' ou 'mensal 2':\n")
        company.payment_schedules.append(new_schedule)
        company.show_schedule_types()


class EditScheduleMenuStrategy(Strategy):

    def show_menu_option(self, company):
        print("Digite o ID do funcionário que deseja alterar a agenda de pagamento:\n")
        company.show_employees(company.employees)
        option = int(input(""))
        selected_employee = [x for x in company.employees if x.id_number == option].pop()
        print("Escolha a nova agenda de pagamento do funcionário: ")
        company.show_schedule_types()
        opt = int(input()) - 1
        selected_employee.set_schedule(company.payment_schedules[opt])