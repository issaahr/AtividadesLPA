# AtividadesLPA

Fiz o upload para salvar os códigos que desenvolvi como atividade da disciplina 'Lógica e Programação de Algoritmos' no primeiro período do curso de Engenharia de Software, para posteriormente revisitá-los mais facilmente caso precise. Deixarei os requisitos das questões a seguir.

## Q1
### Objetivo de aprendizado: Exercitar condicionais simples (if, elif e else).

* Descrição: Código básico que calcula os juros conforme a quantidade de parcelas que o cliente desejar.

* Sobre as parcelas:
  - Se a quantidade de parcelas for menor que 4, o Juros será de 0%;
  - Se a quantidade de parcelas for igual ou maior que 4 e menor que 6, o Juros será de 4%;
  - Se a quantidade de parcelas for igual ou maior que 6 e menor que 9, o Juros será de 8%;
  - Se a quantidade de parcelas for igual ou maior que 9 e menor que 13, o Juros será de 16%;
  - Se a quantidade de parcelas for igual ou maior que 13, o Juros será de 32%.
* Entradas:
  - Foram implementadas entradas para o valor do pedido e a quantidade de parcelas.
* Saídas:
  - Foram implementadas saídas que mostram o nome da loja, o valor individual das parcelas e o valor parcelado.

------
    
## Q2
### Objetivo de aprendizado: Exercitar condicionais (if, elif e/ou else no modelo aninhado) e estruturas de repetição (while, com break e continue).

* Descrição: Código para simular a interface do cliente com um restaurante, mostrando as opções de para pedidos e retornando o valor final.

* Sobre as opções:
  - Tamanho P de Bife Acebolado (BA) custa 16 reais e o Filé de Frango (FF) custa 15 reais;
  -	Tamanho M de Bife Acebolado (BA) custa 18 reais e o Filé de Frango (FF) custa 17 reais;
  - Tamanho G de Bife Acebolado (BA) custa 22 reais e o Filé de Frango (FF) custa 21 reais.
* Entradas:
  - Foram implementadas entradas para o sabor e o tamanho desejado, além de questionar se o cliente deseja mais alguma coisa para, dependendo da resposta, continuar ou quebrar o laço do while.
* Saídas:
  - Foram implementadas saídas que mostram o cardápio, a repetição do que o usuário acabou de escolher e o valor total ao final quebrar o laço.
* Particularidades exigidas pela instituição:
  - Mensagem de erro caso o sabor seja inválido;
  - Mensagem de erro e repetição desde a pergunta do sabor, caso o tamanho seja inválido;
  - O programa deve suportar somar um pedido com duas opções de sabores diferentes.

-----

## Q3
### Objetivo de aprendizado: Exercitar o uso de funções e do bloco try/except dentro do laço while para tratar erros caso o usuário digite um valor diferente das opções mostradas, garantindo que o programa não seja interrompido.

* Descrição:  Código para desenvolver a interface para o funcionário de uma fábrica que vende camisetas no atacado. 

* Sobre as opções de camiseta
  -	Camiseta Manga Curta Simples (MCS), o valor unitário é de um real e oitenta centavos;
  -	Camiseta Manga Longa Simples (MLS), o valor unitário é de dois reais e dez centavos;
  -	Camiseta Manga Curta Com Estampa (MCE), o valor unitário é de dois reais e noventa centavos; 
  -	Camiseta Manga Longa Com Estampa (MLE), o valor unitário é de três reais e vinte centavos. 
* Sobre os descontos conforme a quantidade de camisetas:
  -	Se número de camisetas for menor que 20 não há desconto na venda;
  -	Se número de camisetas for igual ou maior que 20 e menor que 200, o desconto será de 5%;
  -	Se número de camisetas for igual ou maior que 200 e menor que 2000, o desconto será de 7%;
  -	Se número de camisetas for igual ou maior que 2000 e menor ou igual que 20000, o desconto será de 12%;
  -	Se número de camisetas for maior que 20000, não é aceito pedidos nessa quantidade de camisetas.
* Sobre as opções de frete:
  -	Para o adicional de frete por transportadora (1) é cobrado um valor extra de 100 reais;
  -	Para o adicional de frete por Sedex (2) é cobrado um valor extra de 200 reais;
  -	Para o adicional de retirar o pedido na fábrica (0) é cobrado um valor extra de 0 reais.
* Entradas:
  - Foram implementadas entradas para o modelo de camiseta, a quantidade e a opção de frete.
* Saídas:
  - Foram implementadas saídas que mostram o total a pagar com desconto (se houver). Além de mensagens especiais, caso o usuário digite respostas incoerentes para as perguntas.

-----

## Q4
### Objetivo de aprendizado: Exercitar o uso de funções, manipulação de lista, strings e dicionários, estruturas de repetição (while, com estratégias de tratamento de erros e for). Por questão de preferência, implementei os menus com "Match Case", pois considero que o código fica mais claro e legível com ele.

* Descrição: Código para desenvolver o software de gerenciamento de funcionários, com o seguinte menu e opções:
1)	Cadastrar Funcionário
2)	Consultar Funcionário
    1.	Consultar Todos 
    2.	Consultar por Id
    3.	Consultar por setor
    4.	Retornar ao menu
3)	Remover Funcionário
4)	Encerrar Programa

* Entradas:
  - Foram implementadas entradas para navegar pelos menus, e conforme a entrada nos menus, pode-se ter entradas para: Inserir os dados do funcionários ( nome, setor e salário), consultar dados dos funcionários (todos, por id, por setor), remover funcionário por ID ou sair do menu.
* Saídas:
  - Foram implementadas saídas para os menus e dados conforme o usuário solicite.
* Particularidades exigidas pela instituição:
  - O ID do primeiro funcionário deve começar com um número fixo e pré-definido no código, e depois ser autoincrementável para registrar os próximos IDs;
  - O banco de dados deve ser uma lista de dicionários.
