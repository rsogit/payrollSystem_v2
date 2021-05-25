from datetime import datetime
from Models.PaymentMethod.PaymentMethod import PaymentMethod
from Models.PaymentMethod.Deposit import Deposit
from Models.PaymentMethod.InHandsCheck import InHandsCheck
from Models.PaymentMethod.MailCheck import MailCheck
from Models.Employee.Hourly import Hourly
from Models.Employee.Salaried import Salaried
from Models.Employee.Commissioned import Commissioned

id_counting: int = 1
union_id: int = 1
payment_schedules = ["weekly 1 friday", "weekly 2 friday", "monthly $"]


def show_menu():
    print("=======Sistema de Folha de Pagamento========\n")
    print("MENU PRINCIPAL\n")
    print("1 - Cadastrar Funcionário")
    print("2 - Listar Funcionários")
    print("3 - Editar Funcionário")
    print("4 - Remover Funcionário")
    print("5 - Adicionar Cartão de Ponto para um funcionário")
    print("6 - Adicionar Resultado de Venda para um funcionário")
    print("7 - Adicionar Taxa de Servico Sindical para um funcionário")
    print("8 - Rodar folha de pagamento")
    print("9 - Criar agenda de pagamento")
    print("10 - Editar agenda de pagamento de um funcionário")

    print("0 - Sair\n")


def set_payment_method(user_address: str) -> PaymentMethod:
    payment_choice = int(input("Qual o método de pagamento preferido para o funcionário?\n"
                               "1 - Depósito Bancário\n"
                               "2 - Cheque em mãos\n"
                               "3 - Cheque pelos Correios\n"))
    if payment_choice == 1:
        payment_method = Deposit()
    elif payment_choice == 2:
        payment_method = InHandsCheck()
    elif payment_choice == 3:
        opt = input(f'Deseja que o endereco de entrega dos Correios seja "{user_address}"?\n'
                    f'1 - Sim\n'
                    f'2 - Não\n')
        if int(opt) == 1:
            payment_method = MailCheck(user_address)
        elif int(opt) == 2:
            delivery_address = input("Digite o endereco de entrega que deseja: ")
            payment_method = MailCheck(delivery_address)
        else:
            print("O número informado é inválido. Tente novamente.")
    else:
        print("Número inválido, tente novamente")
    return payment_method

## Employees related functions

# Add employee:
# Creates a new employee and add it to the system with the given parameters

def add_employee():

    global id_counting

    name = input("Insira o nome do funcionário: ")
    address = input("Insira o endereço do funcionário: ")

    print("Selecione o número correspondente ao tipo de funcionário: ")
    employee_type = int(input("1. Horista\n"
                              "2. Assalariado\n"
                              "3. Comissionado\n"))
    payment_method = set_payment_method(address)
    if employee_type == 1:
        employee = Hourly(name, address, id_counting, payment_method)
    elif employee_type == 2:
        employee = Salaried(name, address, id_counting, payment_method)
    elif employee_type == 3:
        employee = Commissioned(name, address, id_counting, payment_method)
    else:
        print("Falha no cadastro do novo funcionário, por favor tente novamente respondendo o tipo de 1 a 3.")
        return
    id_counting = id_counting + 1
    employees.append(employee)
    print(f'Total de funcionários: {len(employees)}')
    print("Novo funcionário adicionado com sucesso!\n")


# Edit employee:
# Selects a employee to edit and change its properties in the system.
# The available options for edition are:
# - Name: string with the new name for the employee
# - Type: choose between the three employee types (Hourly, Salaried, Commissioned)
# -------- Hourly: hourly_salary: float
# - Address: string with the new address for the employee
# - Payment Method: choose between the three payment methods.
# ------ Deposit: account: int, agency: int
# ------ MailCheck: address: str
# ------ InHandsCheck
# - Union ID: new id for the employee. The id must be higher than the highest union ID available
# - Union participation: All "employee.union_info" are False by default. In this option you can toggle this attribute.
# - Union tax: float with the value of the monthly tax charged by the union
#

def edit_employee(size, employee_number):
    global union_id
    if employee_number <= size:
        employee = employees[employee_number-1]
        print(f'Digite a opcão que deseja editar do funcionário: {employee.name}')
        print("1 - Nome")
        print("2 - Tipo")
        print("3 - Endereco")
        print("4 - Método de pagamento")
        print("5 - Participacão no sindicato")
        if employee.union_info.is_active:
            print("6 - ID no sindicato")
            print("7 - Taxa sindical fixa")
        try:
            answer = int(input())
        except:
            print("Digite um número válido.")

        if answer == 1:
            new_name = input(f'Digite o novo nome do funcionário "{employee.name}":\n')
            employee.name = new_name
            print("Nome alterado com sucesso")
        elif answer == 2:
            new_type = int(input(f'Selecione o novo tipo do funcionário "{employee.name}":\n'
                                 f'1 - Horista\n'
                                 f'2 - Comissionado\n'
                                 f'3 - Assalariado\n'))
            if new_type == 1:
                employee = Hourly(employee.name,
                                  employee.address,
                                  employee.id_number,
                                  payment_method=employee.payment_method)
                print(f'O funcionário {employee.name} agora é do tipo {employee.type}\n')
            elif new_type == 2:
                employee = Commissioned(employee.name,
                                        employee.address,
                                        employee.id_number,
                                        payment_method=employee.payment_method)
                print(f'O funcionário {employee.name} agora é do tipo {employee.type}\n')
            elif new_type == 3:
                employee = Salaried(employee.name,
                                    employee.address,
                                    employee.id_number,
                                    payment_method=employee.payment_method)
                print(f'O funcionário {employee.name} agora é do tipo {employee.type}\n')
            else:
                print("o funcionário não foi editado, tente novamente.")
                return
        elif answer == 3:
            new_address = input(f'Digite o novo endereco do funcionário: {employee.name}\n')
            employee.address = new_address
            print("Endereco alterado com sucesso")
        elif answer == 4:
            try:
                opt = int(input(f'Selecione o novo método de pagamento do funcionário "{employee.name}":\n'
                                 f'1 - Depósito\n'
                                 f'2 - Cheque em mãos\n'
                                 f'3 - Cheque pelos Correios\n'))
                if opt == 1:
                    employee.payment_method = Deposit()
                elif opt == 2:
                    employee.payment_method = InHandsCheck()
                elif opt == 3:
                    employee.payment_method = MailCheck()
                else:
                    print("Por favor, selecione uma opção válida")
            except:
                print("Por favor, selecione uma opção válida")
        elif answer == 5:
            if employee.union_info.is_active:
                opt = int(input(f'Atualmente o funcionário {employee.name} está ativo no sindicato, '
                            f'deseja deixá-lo inativo?\n'
                      f'1 - Sim\n'
                      f'2 - Não\n'))
            else:
                opt = int(input(f'Atualmente o funcionário {employee.name} está inativo no sindicato, '
                            f'deseja deixá-lo ativo?\n'
                      f'1 - Sim\n'
                      f''f'2 - Não\n'))
                employee.union_info.union_id = union_id
                union_id = union_id + 1
            if opt == 1:
                employee.union_info.is_active = True
            elif opt == 2:
                employee.union_info.is_active = False
                if not (employee.union_info.monthly_tax > 0):
                    new_taxes = float(input("Adicione a taxa mensal fixa do sindicato para esse funcionário: R$ "))
                    employee.union_info.monthly_tax = new_taxes
            else:
                print("Entrada inválida, tente novamente.")
        elif answer == 6:
            try:
                opt = int(input(f"Digite um número inteiro maior que {union_id} para ser seu novo ID do Sindicato: "))
                if opt > union_id:
                    employee.union_info.union_id = opt
                else:
                    print(f"O novo ID precisa ser maior que {union_id}. Tente novamente.")
            except:
                print("Entrada inválida. Tente novamente.")
        elif answer == 7:
            try:
                new_taxes = float(input("Adicione a nova taxa mensal fixa do sindicato para esse funcionário: R$ "))
                employee.union_info.monthly_tax = new_taxes
            except:
                print("Entrada inválida. Tente novamente.")
        elif answer == 8:
            print("Voltando para o menu principal...")
        elif answer > 8:
            print("Por favor, selecione um número válido")
        else:
            print("Retornando ao menu principal...")

# Delete Employee:
# Deletes the given employee from the system


def delete_employee(size, employee_number):
    if size != 0:
        for index, employee in enumerate(employees):
            if employee.id_number == employee_number:
                deleted_employee = employees.pop(index)
                print(f'Funcionário "{deleted_employee.name}" deletado com sucesso!')

# Show employees functions:
# functions used to show and list employees according to its types


def show_all_employees(employees):
    for employee in employees:
        print(f'{employee.id_number} - {employee.name}')


def show_employees(employees_array, employee_type):
    employees_array = [x for x in employees_array if x.type == employee_type]
    for employee in employees_array:
        print(f'{employee.id_number} - {employee.name}')


def show_union_employees(employees_array):
    for employee in employees_array:
        print(f'{employee.union_info.union_id} - {employee.name}')


def show_employee_details(employee):
    print("______________________________________")
    print(f'Nome: {employee.name}')
    print(f'Tipo: {employee.type}')
    print(f'Endereco: {employee.address}')
    print("______________________________________")


def show_schedule_types():
    print("Essas são as agendas de pagamento atuais: \n")
    for index, schedule in enumerate(payment_schedules):
        print(f'{index+1} - {schedule}')

# Get employees:
# functions used to get employees according to its types and properties


def get_union_employees(employees_array):
    employees_array = [x for x in employees_array if x.union_info.is_active]
    return employees_array


def get_employee_by_id(employees, employee_id):
    return [x for x in employees if x.id_number == employee_id]


# Pay employees:
# Functions related to the payroll. Used to pay each employee with the appropriate methods and values.


def run_payroll(employees):
    for emp in employees:
        emp.calculate_salary()

# get_payroll:
# Lista os usuários que devem receber pagamento para o dia indicado. O usuário do sistema tem a opcao de rodar a folha
# de pagamento para o dia atual ou escolher uma data para rodar.
# Se o usuário escolher pagar os usuários informados pela funcão, a saída sera os contracheques de todos os
# empregados pagos para aquele dia.


def get_payroll(employees_array, pay_date):
    scheduled_employees = []
    for employee in employees_array:
        if employee.schedule[0].date() == pay_date.date():
            scheduled_employees.append(employee)

    if len(scheduled_employees) > 0:
        print(f'Os seguintes funcionários estão agendados para a folha de pagamento referente à {pay_date.date()}')
        for emp in scheduled_employees:
            print(f'{emp.id_number} - {emp.name}')
        print("Deseja confirmar o pagamento para esses funcionários?\n"
              "1 - Sim\n"
              "2 - Não\n")
        opt = int(input())
        if opt == 1:
            run_payroll(scheduled_employees)
        elif opt == 2:
            print("Certo, volte aqui quando quiser realizar o pagamento.")
    else:
        print("Nenhum funcionário está agendado para a folha de pagamento de hoje.")


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
        show_menu()

        options = int(input("Selecione a opcão que deseja acessar: "))
        if options == 1:
            add_employee()
        elif options == 2:
            if len(employees) != 0:
                show_all_employees(employees)
            else:
                print("Não há funcionários cadastrados")
        elif options == 3:
            print("Digite o ID do funcionário que deseja editar: ")
            show_all_employees(employees)
            employee_number = int(input("\n"))
            edit_employee(len(employees), employee_number)
        elif options == 4:
            print("Digite o ID do funcionário que deseja deletar: ")
            show_all_employees(employees)
            employee_number = int(input("\n"))
            delete_employee(len(employees), employee_number)
        elif options == 5:
            print("Digite o ID do funcionário que deseja adicionar o Cartão de Ponto:\n")
            show_employees(employees, "Horista")
            option = int(input(""))
            selected_employee = get_employee_by_id(employees, option).pop()
            selected_employee.add_timecard()
        elif options == 6:
            print("Digite o ID do funcionário que deseja adicionar o Resultado de Venda:\n")
            show_employees(employees, "Comissionado")
            option = int(input(""))
            selected_employee = get_employee_by_id(employees, option).pop()
            selected_employee.add_sale()
        elif options == 7:
            print("Digite o ID do funcionário que deseja adicionar a Taxa de Servico Sindical:\n")
            union_employees = get_union_employees(employees)
            if len(union_employees) > 0:
                show_union_employees(union_employees)
                option = int(input(""))
                selected_employee = get_employee_by_id(employees, option).pop()
                selected_employee.union_info.add_service_fee()
            else:
                print("Não há funcionários ativos no sindicato")
        elif options == 8:
            print("Deseja rodar a folha de pagamento para hoje ou outro dia?\n"
                  "1 - Rodar para hoje\n"
                  "2 - Rodar para outra data")
            opt = int(input())
            if opt == 1:
                run_payroll(employees, datetime.now())
            elif opt == 2:
                fmt = "%d/%m/%Y"
                try:
                    run_date = input("Digite a data que deseja rodar a folha de pagamento, "
                                                       "no formato DD/MM/AAAA: ")
                    run_date = datetime.strptime(run_date, fmt)
                except:
                    print("Data inválida, rodando folha de pagamento para hoje: ")
                    run_date = datetime.now()
                get_payroll(employees, run_date)
        elif options == 9:
            new_schedule = input("Por favor digite a nova agenda de pagamentos que deseja adicionar, "
                                 "como no exemplo 'weekly 3 monday' ou 'mensal 2':\n")
            payment_schedules.append(new_schedule)
            show_schedule_types()
        elif options == 10:
            print("Digite o ID do funcionário que deseja alterar a agenda de pagamento:\n")
            show_all_employees(employees)
            option = int(input(""))
            selected_employee = get_employee_by_id(employees, option).pop()
            print("Escolha a nova agenda de pagamento do funcionário: ")
            show_schedule_types()
            opt = int(input()) - 1
            selected_employee.set_schedule(payment_schedules[opt])
        elif options == 0:
            running = False
            print("Exiting\n")
