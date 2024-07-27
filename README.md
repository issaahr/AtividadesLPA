### AtividadesLPA

Fiz upload salvar os códigos que fiz como atividade da disciplina "Lógica e Programação de Algoritmos" no primeiro período do curso Engenharia de Software. Deixarei os requisitos das questões a seguir.

# Q1
Código básico que calcula os juros conforme a quantidade de parcelas que o cliente desejar.

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
    
# Q2
Código para simular a interface do cliente com um restaurante, mostrando as opções de para pedidos e retornando o valor final.

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
