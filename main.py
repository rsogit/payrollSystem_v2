from Models.PaymentMethod.Deposit import Deposit
from Models.PaymentMethod.InHandsCheck import InHandsCheck
from Models.PaymentMethod.MailCheck import MailCheck
from Models.Employee.Hourly import Hourly
from Models.Employee.Salaried import Salaried
from Models.Employee.Commissioned import Commissioned
from Utils.MainMenuStrategy import *
from Models.Company import Company


id_counting: int = 1


def initialize_employees():
    global id_counting

    emp1 = Hourly("Funcionário 1", "Primeiro endereco", 1, payment_method=Deposit(agency=1245, account=456), hourly_salary=12)
    emp2 = Salaried("Funcionário 2", "Segundo endereco", 2, payment_method=MailCheck(), salary=2000)
    emp3 = Commissioned("Funcionário 3", "Terceiro endereco", 3, payment_method=InHandsCheck(), salary=2000, percentage=12)
    employees.append(emp1)
    employees.append(emp2)
    employees.append(emp3)

    id_counting = len(employees) + 1


if __name__ == '__main__':

    print('Welcome to the payroll System program')
    running = True
    employees = []

    # Uncomment the line above to use pre-made employees or add it yourself using the system
    initialize_employees()

    while running:
        company = Company("UFAL")
        company.show_menu()
        company.employees = employees
        company.id_counting = id_counting

        options = int(input("Selecione a opção que deseja acessar: "))
        if options == 1:
            context = MainMenuStrategy(AddEmployeeMenuStrategy())
        elif options == 2:
            context = MainMenuStrategy(ListEmployeeMenuStrategy())
        elif options == 3:
            context = MainMenuStrategy(EditEmployeeMenuStrategy())
        elif options == 4:
            context = MainMenuStrategy(RemoveEmployeeMenuStrategy())
        elif options == 5:
            context = MainMenuStrategy(AddTimeCardMenuStrategy())
        elif options == 6:
            context = MainMenuStrategy(AddSaleResultMenuStrategy())
        elif options == 7:
            context = MainMenuStrategy(AddServiceFeeMenuStrategy())
        elif options == 8:
            context = MainMenuStrategy(RunPayrollMenuStrategy())
        elif options == 9:
            context = MainMenuStrategy(AddScheduleMenuStrategy())
        elif options == 10:
            context = MainMenuStrategy(EditScheduleMenuStrategy())
        elif options == 0:
            running = False
            print("Exiting\n")

        context.show_menu_option(company)
