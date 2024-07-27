print("-" * 7 + "Bem-vindo a loja de marmitas da Issah" + "-" * 7)
print("-" * 31 + "Cardápio" + "-" * 31)
print("-" * 70)
print("-" * 7 + "|  Tamanho |" + " Bife Acebolado (BA)" + " | Filé de Frango (FF) |" + "-" * 7)
print("-" * 7 + "|     P    |" + "      R$ 16,00      " + " |       R$ 15,00      |" + "-" * 7)
print("-" * 7 + "|     M    |" + "      R$ 18,00      " + " |       R$ 17,00      |" + "-" * 7)
print("-" * 7 + "|     G    |" + "      R$ 22,00      " + " |       R$ 21,00      |" + "-" * 7)
print("-" * 70)

valor = 0

while True:
    # Entrada das opções (sabor, tamanho)
    sabor = input("Entre com o sabor desejado (BA/FF): ")
    # Condicional pra verificar se a entrada é a esperada
    if sabor != "BA" and sabor != "FF":
        print("Sabor inválido. Tente novamente")
        continue
    tamanho = input("Entre com o tamanho desejado (P/M/G): ")
    # Condicional pra verificar se a entrada é a esperada
    if tamanho != "P" and tamanho != "M" and tamanho != "G":
        print("Tamanho inválido. Tente novamente")
        continue

    if sabor == "BA":
        if tamanho == "P":
            print("Você pediu um bife acebolado no tamanho P: R$ 16,00")
            valor += 16
        elif tamanho == "M":
            print("Você pediu um bife acebolado no tamanho M: R$ 18,00")
            valor += 18
        elif tamanho == "G":
            print("Você pediu um bife acebolado no tamanho G: R$ 22,00")
            valor += 22

    if sabor == "FF":
        if tamanho == "P":
            print("Você pediu um filé de frango no tamanho P: R$ 15,00")
            valor += 15
        elif tamanho == "M":
            print("Você pediu um filé de frango no tamanho M: R$ 17,00")
            valor += 17
        elif tamanho == "G":
            print("Você pediu um filé de frango no tamanho G: R$ 21,00")
            valor += 21

    algomais = input("\nDeseja mais alguma coisa (S/N):")
    # Saltar linha
    print()
    if algomais == "S":
        continue
    else:
        break
print(f"O valor total a ser pago é de: R$ {valor:.2f}")
