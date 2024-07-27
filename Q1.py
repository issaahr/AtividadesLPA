print("Bem-vindo a Loja da Issah")

# Requisição do valor do pedido e quantidade de parcelas
valorDoPedido = float(input("Entre com o valor do pedido: "))
quantidadeParcelas = int(input("Entre com a quantidade de parcelas: "))

# Condicionais para definir o valor dos juros com base na quantidade de parcelas
if 4 <= quantidadeParcelas < 6:
    # 4% de juros
    juros = 0.04
elif 6 <= quantidadeParcelas < 9:
    # 8% de juros
    juros = 0.08
elif 9 <= quantidadeParcelas < 13:
    # 16% de juros
    juros = 0.16
elif quantidadeParcelas >= 13:
    # 32% de juros
    juros = 0.32
else:
    juros = 0

# Cálculos
valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas

# Saída
print(f"O valor das parcelas é de R$ {valorDaParcela:.2f}")
print(f"O o total do valor parcelado é de R$ {valorTotalParcelado:.2f}")
