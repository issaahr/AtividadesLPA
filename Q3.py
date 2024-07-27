def escolha_modelo():
    """
    Função para atribuir o valor unitário dependendo da escolha de camiseta do usuário
    """
    while True:
        # Garante que os dados ficarão em letras maiusculas
        modelo_camiseta = input(">> ").upper()
        if modelo_camiseta == "MCS":
            valor_unitario_camiseta = 1.80
        elif modelo_camiseta == "MLS":
            valor_unitario_camiseta = 2.10
        elif modelo_camiseta == "MCE":
            valor_unitario_camiseta = 2.90
        elif modelo_camiseta == "MLE":
            valor_unitario_camiseta = 3.20
        else:
            print("Escolha inválida, entre com o modelo novamente")
            continue
        return valor_unitario_camiseta


def num_camisetas():
    """
    Função que usa o número de camisetas para calcular o desconto,
    retornando para o cálculo apenas as camisetas que serão pagas
    """
    while True:
        try:
            qte_camisetas = int(input("Entre com o número de camisetas: "))
            # Trata casos onde o usuário digita 0 ou um valor menor
            if qte_camisetas <= 0:
                print("O número de camisetas precisa ser de no mínimo uma unidade")
                continue
            elif qte_camisetas < 20:
                # Sem desconto
                qte_camisetas_pagas = qte_camisetas
            elif 20 <= qte_camisetas < 200:
                # 5% de desconto
                qte_camisetas_pagas = qte_camisetas * 0.95
            elif 200 <= qte_camisetas < 2000:
                # 7% de desconto
                qte_camisetas_pagas = qte_camisetas * 0.93
            elif 2000 <= qte_camisetas < 20000:
                # 12% de desconto
                qte_camisetas_pagas = qte_camisetas * 0.88
            else:
                print("Não aceitamos tantas camisetas de uma vez")
                print("Por favor, entre com o número de camisetas novamente.")
                # Repete a pergunta sobre a quantidade em casos iguais ou superiores a 20000
                continue
        except ValueError:
            print("Entrada inválida, por favor, insira um valor numérico")
            # Repete a pergunta sobre a quantidade em casos onde a entrada não for um número inteiro
            continue
        else:
            return qte_camisetas_pagas


def frete():
    """
    Função responsável por calcular o frete
    """
    print("Escolha o tipo de frete: ")
    print("1 - Frete por transportadora - R$ 100,00")
    print("2 - Frete por Sedex - R$ 200,00")
    print("0 - Retirar pedido na fábrica - R$ 0,00")
    while True:
        try:
            opcao_frete = int(input(">> "))
            if opcao_frete == 1:
                valor_frete = 100
            elif opcao_frete == 2:
                valor_frete = 200
            elif opcao_frete == 0:
                valor_frete = 0
            else:
                print("Digite um número entre 0 e 2")
                continue
        except ValueError:
            # Trata casos onde o usuário não digitou um número inteiro
            print("Entrada inválida, digite 0, 1 ou 2")
        else:
            return valor_frete


# MAIN
print("Bem vindo a fábrica de camisetas da Issah")

print("Entre com o modelo desejado: ")
print("MCS - Manga Curta Simples")
print("MLS - Manga Longa Simples")
print("MCE - Manga Curta Estampada")
print("MLE - Manga Longa Estampada")

valorUnitario = escolha_modelo()
qteCamisetasPagas = num_camisetas()
valorFrete = frete()

ValorTotalPagar = (valorUnitario * qteCamisetasPagas) + valorFrete
print(f"Total: R$ {ValorTotalPagar:.2f} (Modelo: R$ {valorUnitario:.2f} * Quantidade (com desconto): {qteCamisetasPagas:.0f} + frete: R$ {valorFrete:.2f} )")
