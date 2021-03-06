# Sistema de folha de pagamento

Rodando o projeto
-------
Primeiro, rode os comandos abaixo no terminal:

    $ git clone git@github.com:rsogit/payrollSystem_v2.git
    $ cd payrollSystem_v2

Instale as dependências:

	$ pip install -r requirements.txt

---
# Resumo

O objetivo do projeto é construir um sistema de folha de pagamento. O sistema consiste do
gerenciamento de pagamentos dos empregados de uma empresa. Além disso, o sistema deve
gerenciar os dados destes empregados, a exemplo os cartões de pontos. Empregados devem receber
o salário no momento correto, usando o método que eles preferem, obedecendo várias taxas e
impostos deduzidos do salário.
* Alguns empregados são horistas. Eles recebem um salário por hora trabalhada. Eles
submetem "cartões de ponto" todo dia para informar o número de horas trabalhadas naquele
dia. Se um empregado trabalhar mais do que 8 horas, deve receber 1.5 a taxa normal
durante as horas extras. Eles são pagos toda sexta-feira.
* Alguns empregados recebem um salário fixo mensal. São pagos no último dia útil do mês
(desconsidere feriados). Tais empregados são chamados "assalariados".
* Alguns empregados assalariados são comissionados e portanto recebem uma comissão, um
percentual das vendas que realizam. Eles submetem resultados de vendas que informam a
data e valor da venda. O percentual de comissão varia de empregado para empregado. Eles
são pagos a cada 2 sextas-feiras; neste momento, devem receber o equivalente de 2 semanas
de salário fixo mais as comissões do período.
  * Empregados podem escolher o método de pagamento.
  * Podem receber um cheque pelos correios
  * Podem receber um cheque em mãos
  * Podem pedir depósito em conta bancária
  * Alguns empregados pertencem ao sindicato (para simplificar, só há um possível sindicato).
O sindicato cobra uma taxa mensal do empregado e essa taxa pode variar entre
empregados. A taxa sindical é deduzida do salário. Além do mais, o sindicato pode
ocasionalmente cobrar taxas de serviços adicionais a um empregado. Tais taxas de serviço
são submetidas pelo sindicato mensalmente e devem ser deduzidas do próximo
contracheque do empregado. A identificação do empregado no sindicato não é a mesma da
identificação no sistema de folha de pagamento.
* A folha de pagamento é rodada todo dia e deve pagar os empregados cujos salários vencem
naquele dia. O sistema receberá a data até a qual o pagamento deve ser feito e calculará o
pagamento para cada empregado desde a última vez em que este foi pago.


Func | Título | Breve descrição
------------ | ------------- | -------------  
**1** (Feito)| Adição de um empregado | Um novo empregado é adicionado ao sistema. Os seguintes atributos são fornecidos: nome, endereço, tipo (_hourly_, _salaried_, _commissioned_) e os atributos associados (salário horário, salário mensal, comissão). Um número de empregado (único) deve ser escolhidoautomaticamente pelo sistema.
**2** (Feito) | Remoção de um empregado | Um empregado é removido do sistema.
**3** (Feito) | Lançar um Cartão de Ponto | O sistema anotará a informação do cartão de ponto e a associará ao empregado correto.
**4** (Feito) | Lançar um Resultado Venda | O sistema anotará a informação do resultado da venda e a associará ao empregado correto.
**5** (Feito) | Lançar uma taxa de serviço | O sistema anotará a informação da taxa de serviço e a  associará ao empregado correto. 
**6** (Feito) | Alterar detalhes de um empregado | Os seguintes atributos de um empregado podem ser  alterados: nome, endereço, tipo (_hourly_, _salaried_, _commisioned_), método de pagamento, se pertence ao sindicato ou não, identificação no sindicato, taxa sindical. 
**7** (Feito) | Rodar a folha de pagamento para hoje | O sistema deve achar todos os empregados que devem  ser pagos no dia indicado, deve calcular o valor do salário  e deve providenciar o pagamento de acordo com o método escolhido pelo empregado
**8** (Não feito) | Undo/redo | Qualquer transação associada as funcionalidades **1** a **7**  deve ser _desfeita_ (*undo*) ou _refeita_ (*redo*).
**9** (Feito) | Agenda de Pagamento | Cada empregado é pago de acordo com uma "_agenda de  pagamento_". Empregados podem selecionar a agenda de  pagamento que desejam. Por _default_, as agendas  "_semanalmente_", "_mensalmente_" e "_bi-semanalmente_" são usadas, como explicado na descrição geral. Posteriormente, um empregado pode pedir para ser pago de acordo com qualquer uma dessas agendas.
**10** (Feito) | Criação de Novas Agendas de Pagamento | A direção da empresa pode criar uma nova agenda de  pagamento e disponibilizá-la para os empregados  escolherem, se assim desejarem. Uma agenda é especificada através de um string. Alguns exemplos  mostram as possibilidades: "**mensal 1**": _dia 1 de todo mês_ ; "**mensal $**": _último dia útil de todo mês_; "**semanal 1 segunda**": _toda semana  às segundas-feiras_; "**semanal 2 segunda**": _a cada 2 semanas às segundas-feiras_ ; etc.
---
# Code Smells

No menu principal (main.py), havia uma cadeia de condicionais que dificultavam a manutenção e entendimento do menu e tornava o código repetido e sujo. 
Apliquei o padrão Strategy para tratar cada parte do menu de funcionalidades de forma separada por meio da interface MainMenuStrategy.

Além disso, encontrei os seguintes code smells:
- [Long Method](https://sourcemaking.com/refactoring/smells/long-method) 
  - editEmployee em Company.py;
  - set_schedule em Employee.py;

- [Duplicate Code](https://sourcemaking.com/refactoring/smells/duplicate-code)
  - Na função main
  - Na estrutura de menus

- [Data Class](https://sourcemaking.com/refactoring/smells/data-class)
  - As classes Sales e Timecard se encaixam no code smell "Data Class" pois só contém propriedades e métodos de acesso.


----
# Refactor

### Strategy

O padrão *Strategy* foi usado para resolver o problema da cadeia de condicionais e lidar com os diferentes tipos de estratégias requeridas nesse menu para acesso das funcionalidades. Para isso foi criado uma classe MainMenuStrategy que serve como contexto para as classes Strategy que representam as funcionalidade principais do sistema e as apresentam no menu.


### Long Method:
- Método editEmployee da classe Main era muito extenso.
  - Refatoração: foi dividido em sete outros métodos auxiliares para melhorar a visibilidade e manutenção do método.
  

- Método set_schedule da classe Employee era muito extenso.
  - Refatorado: foi divido em três outros métodos auxiliares para melhorar a visibilidade e manutenção do método. 
    
Nos dois casos, os padrões aplicados nos métodos foram:
- [Decompose Conditional](https://sourcemaking.com/refactoring/decompose-conditional)
- [Extract Method](https://sourcemaking.com/refactoring/extract-method)

Além disso, após a refatoração, os tratamentos de erro do método também pararam de estar duplicados

### Middle Man
Os métodos get_union_employees, show_all_employees, get_employee_by_id tinha o code smell [Middle Man](https://sourcemaking.com/refactoring/smells/middle-man), que se caracteriza por métodos "de uma linha" que tem pouca utilidade real. Esse problema foi solucionado colocando a linha de código diretamente no método os chama.

