
from Models.PaymentMethod.PaymentMethod import PaymentMethod
from Models.PaymentMethod.Deposit import Deposit
from Models.PaymentMethod.InHandsCheck import InHandsCheck
from Models.PaymentMethod.MailCheck import MailCheck
from Models.Employee.Hourly import Hourly
from Models.Employee.Salaried import Salaried
from Models.Employee.Commissioned import Commissioned


class Company:
    id_counting: int = 1
    union_id: int = 1
    payment_schedules = ["weekly 1 friday", "weekly 2 friday", "monthly $"]

    def __init__(self, company_name):
        self.employees = []
        self.company_name = company_name

    def set_payment_method(self, user_address: str) -> PaymentMethod:
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


    def show_menu(self):
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

    # Add employee:
    # Creates a new employee and add it to the system with the given parameters

    def add_employee(self):

        name = input("Insira o nome do funcionário: ")
        address = input("Insira o endereço do funcionário: ")

        print("Selecione o número correspondente ao tipo de funcionário: ")
        employee_type = int(input("1. Horista\n"
                                  "2. Assalariado\n"
                                  "3. Comissionado\n"))
        payment_method = self.set_payment_method(address)
        if employee_type == 1:
            employee = Hourly(name, address, self.id_counting, payment_method)
        elif employee_type == 2:
            employee = Salaried(name, address, self.id_counting, payment_method)
        elif employee_type == 3:
            employee = Commissioned(name, address, self.id_counting, payment_method)
        else:
            print("Falha no cadastro do novo funcionário, por favor tente novamente respondendo o tipo de 1 a 3.")
            return
        self.id_counting = self.id_counting + 1
        self.employees.append(employee)
        print(f'Total de funcionários: {len(self.employees)}')
        print("Novo funcionário adicionado com sucesso!\n")

    # Edit employee:
    # Selects a employee to edit and change its properties in the system.

    def edit_employee_name(self, employee):
        new_name = input(f'Digite o novo nome do funcionário "{employee.name}":\n')
        employee.name = new_name
        print("Nome alterado com sucesso")

    def edit_employee_type(self, employee):
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

    def edit_employee_address(self, employee):
        new_address = input(f'Digite o novo endereco do funcionário: {employee.name}\n')
        employee.address = new_address
        print("Endereco alterado com sucesso")

    def edit_employee_payment_method(self, employee):
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

    def edit_employee_union_participation(self, employee):

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
            employee.union_info.union_id = self.union_id
            self.union_id = self.union_id + 1
        if opt == 1:
            employee.union_info.is_active = True
        elif opt == 2:
            employee.union_info.is_active = False
            if not (employee.union_info.monthly_tax > 0):
                new_taxes = float(input("Adicione a taxa mensal fixa do sindicato para esse funcionário: R$ "))
                employee.union_info.monthly_tax = new_taxes
        else:
            print("Entrada inválida, tente novamente.")

    def edit_employee_union_id(self, employee):
        opt = int(input(f"Digite um número inteiro maior que {self.union_id} para ser seu novo ID do Sindicato: "))
        if opt > self.union_id:
            employee.union_info.union_id = opt
        else:
            print(f"O novo ID precisa ser maior que {self.union_id}. Tente novamente.")
        print("Entrada inválida. Tente novamente.")

    def edit_employee_union_fee(self, employee):
        new_taxes = float(input("Adicione a nova taxa mensal fixa do sindicato para esse funcionário: R$ "))
        employee.union_info.monthly_tax = new_taxes
        print("Entrada inválida. Tente novamente.")

    def edit_employee(self, size, employee_number):
        if employee_number <= size:
            employee = self.employees[employee_number - 1]
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
            try:
                if answer == 1:
                    self.edit_employee_name(employee)
                elif answer == 2:
                    self.edit_employee_type(employee)
                elif answer == 3:
                    self.edit_employee_address(employee)
                elif answer == 4:
                    self.edit_employee_payment_method(employee)
                elif answer == 5:
                    self.edit_employee_union_participation(employee)
                elif answer == 6:
                    self.edit_employee_union_id(employee)
                elif answer == 7:
                    self.edit_employee_union_fee(employee)
                elif answer == 8:
                    print("Voltando para o menu principal...")
                elif answer > 8:
                    print("Por favor, selecione um número válido")
                else:
                    print("Retornando ao menu principal...")
            except:
                print("Entrada inválida. O funcionário não foi editado, tente novamente.")

    # Delete Employee:
    # Deletes the given employee from the system

    def delete_employee(self, size, employee_number):
        if size != 0:
            for index, employee in enumerate(self.employees):
                if employee.id_number == employee_number:
                    deleted_employee = self.employees.pop(index)
                    print(f'Funcionário "{deleted_employee.name}" deletado com sucesso!')

    # Show employees functions:
    # functions used to show and list employees according to its types

    def show_employees(self, employees_array, employee_type=None):
        if employee_type is not None:
            employees_array = [x for x in employees_array if x.type == employee_type]
        for employee in employees_array:
            print(f'{employee.id_number} - {employee.name}')

    def show_union_employees(self, employees_array):
        for employee in employees_array:
            print(f'{employee.union_info.union_id} - {employee.name}')

    def show_employee_details(self, employee):
        print("______________________________________")
        print(f'Nome: {employee.name}')
        print(f'Tipo: {employee.type}')
        print(f'Endereco: {employee.address}')
        print("______________________________________")

    def show_schedule_types(self):
        print("Essas são as agendas de pagamento atuais: \n")
        for index, schedule in enumerate(self.payment_schedules):
            print(f'{index + 1} - {schedule}')

    # Pay employees:
    # Functions related to the payroll. Used to pay each employee with the appropriate methods and values.

    def run_payroll(self, employees):
        for emp in employees:
            emp.calculate_salary()

    # get_payroll:
    # Lista os usuários que devem receber pagamento para o dia indicado. O usuário do sistema tem a opcao de rodar a folha
    # de pagamento para o dia atual ou escolher uma data para rodar.
    # Se o usuário escolher pagar os usuários informados pela funcão, a saída sera os contracheques de todos os
    # empregados pagos para aquele dia.

    def get_payroll(self, employees_array, pay_date):
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
                self.run_payroll(scheduled_employees)
            elif opt == 2:
                print("Certo, volte aqui quando quiser realizar o pagamento.")
        else:
            print("Nenhum funcionário está agendado para a folha de pagamento de hoje.")