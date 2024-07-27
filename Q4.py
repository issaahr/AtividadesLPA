def formatar_titulo(texto, largura_total=50, simbolo='-'):
    """
    Função que enfeita o menu de acordo com o tamanho da palavra recebida como parâmetro
    """
    largura_texto = len(texto)
    largura_tracos = (largura_total - largura_texto) // 2
    linha_formatada = simbolo * largura_tracos + texto + simbolo * largura_tracos

    if len(linha_formatada) < largura_total:
        linha_formatada += simbolo

    return linha_formatada


def cadastrar_funcionario(id_f):
    """
    Função responsável por inserir os dados dos funcionários na lista lista_funcionarios
    Recebe um id pré-definido como parâmetro
    """
    menu_cadastro = formatar_titulo(" MENU CADASTRAR FUNCIONARIO ", 50, '-')
    print()
    # Insere traços conforme o tamanho da variável dentro de len()
    print("-" * len(menu_cadastro))
    print(menu_cadastro)
    print(f"Id: {id_f}")
    nome_f = input("Por favor, entre com o nome do Funcionário: ").capitalize()
    setor_f = input("Por favor, entre com o setor do Funcionário: ")
    salario_f = float(input("Por favor, entre com o salário do Funcionário: "))

    funcionario = {
        "id":  id_f,
        "nome": nome_f,
        "setor": setor_f,
        "salario": salario_f
    }
    lista_funcionarios.append(funcionario.copy())
    print("Funcionário cadastrado com sucesso!\n")


def consultar_funcionarios():
    """
    Função responsável por fazer a consulta dos funcionários de acordo com a opção desejada
    """
    while True:
        try:
            menu_consulta = formatar_titulo(" MENU CONSULTAR FUNCIONARIO ", 50, '-')
            print()
            # Insere traços conforme o tamanho da variável dentro de len()
            print("-" * len(menu_consulta))
            print(menu_consulta)

            print("Escolha a opção desejada: ")
            print("1 - Consultar todos os Funcionários")
            print("2 - Consultar Funcionário por ID")
            print("3 - Consultar Funcionário(s) por setor")
            print("4 - Retornar ao menu")

            escolha_cons = int(input(">> "))

            print("-" * 50)
            print()
            match escolha_cons:
                # Todos os funcionários
                case 1:
                    for funcionario in lista_funcionarios:
                        for chave, valor in funcionario.items():
                            print(f"{chave.capitalize()}: {valor}")
                        print()
                    print()
                # Por ID
                case 2:
                    id_cons = int(input("Digite o ID do funcionário: "))
                    existencia_funcionario = False
                    for funcionario in lista_funcionarios:
                        if funcionario.get("id") == id_cons:
                            existencia_funcionario = True
                            for chave, valor in funcionario.items():
                                print(f"{chave.capitalize()}: {valor}")
                            print()
                    if not existencia_funcionario:
                        print("Este funcionário não está cadastrado")
                        continue
                # Por setor
                case 3:
                    setor_cons = input("Digite o setor do(s) funcionário(s): ").upper()
                    existencia_funcionario = False
                    for funcionario in lista_funcionarios:
                        # upper() para comparação com todas em letra maiuscula
                        if funcionario.get("setor").upper() == setor_cons:
                            existencia_funcionario = True
                            for chave, valor in funcionario.items():
                                print(f"{chave.capitalize()}: {valor}")
                            print()
                    if not existencia_funcionario:
                        print("Não existem funcionários neste setor")
                        continue
                case 4:
                    return
                case _:
                    # Para tratar números inteiros fora da faixa
                    print("Opção inválida")
                    continue
        # Para que o programa não falhe por entrada diferente de n° inteiro
        except ValueError:
            print("Entrada inválida, tente novamente!")
            continue


def remover_funcionario():
    """
    Função responsável por fazer a remoção de um funcionário utilizando a ID
    """
    menu_remocao = formatar_titulo(" MENU REMOVER FUNCIONARIO ", 50, '-')
    # Insere traços conforme o tamanho da variável dentro de len()
    print("-" * len(menu_remocao))
    print(menu_remocao)

    while True:
        try:
            id_remocao = int(input("Digite o ID do funcionário: "))
            existencia_funcionario = False
            for funcionario in lista_funcionarios:
                if funcionario.get("id") == id_remocao:
                    lista_funcionarios.remove(funcionario)
                    print(f"Funcionário com ID {id_remocao} removido com sucesso.")
                    print("")
                    return
            if not existencia_funcionario:
                print("ID inválido. Funcionário não encontrado!\n")
                continue
        except ValueError:
            print("ID inválido. Digite um número inteiro!\n")
            continue


# Função Principal

# ID inicial é conforme requisitado pela instituição
id_global = 4699663
lista_funcionarios = []

while True:
    try:
        print("Bem vindo a Empresa da Issah")
        imprime_menu = formatar_titulo(" MENU PRINCIPAL ", 50, '-')
        # Insere traços conforme o tamanho da variável dentro de len()
        print("-" * len(imprime_menu))
        print(imprime_menu)

        print("Escolha a opção desejada: ")
        print("1 - Cadastrar Funcionários")
        print("2 - Consultar Funcionário(s)")
        print("3 - Remover Funcionário")
        print("4 - Sair")

        escolha = int(input(">> "))

        match escolha:
            case 1:
                cadastrar_funcionario(id_global)
                # Incremento no id do próximo funcionario cadastrado
                id_global += 1
            case 2:
                consultar_funcionarios()
            case 3:
                remover_funcionario()
            case 4:
                print("Saindo...")
                break
            case _:
                # Trata casos onde o usuario digita um n° inteiro fora da faixa
                print("Opção inválida! \n")
                continue
    except ValueError:
        # Trata casos onde o usuário digita algo diferente de um número inteiro
        print("Opção inválida. Digite um número inteiro!\n")
