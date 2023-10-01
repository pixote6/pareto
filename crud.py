def incluir_venda(vendas):
    print("Escolha o tipo de televisão:")
    print("1 - Televisão LCD")
    print("2 - Televisão LED")
    print("3 - Televisão Tubo")
    
    opcao_televisao = input("Digite o número correspondente ao tipo de televisão: ")
    
    if opcao_televisao == '1':
        tipo_televisao = "LCD"
    elif opcao_televisao == '2':
        tipo_televisao = "LED"
    elif opcao_televisao == '3':
        tipo_televisao = "Tubo"
    else:
        print("Opção inválida. Registrando como 'Outro'")
        tipo_televisao = "Outro"
    
    valor_venda = float(input("Digite o valor da venda: R$"))

    venda_info = f"{tipo_televisao},{valor_venda:.2f}"

    vendas.append(venda_info)
    print("Venda registrada com sucesso!")

def exibir_vendas(vendas):
    print("\nVendas registradas:")
    for i, venda in enumerate(vendas, start=1):
        tipo_televisao, valor_venda = venda.split(',')
        print(f"{i} - Tipo: {tipo_televisao}, Valor: R${valor_venda}")

def editar_vendas(vendas):
    exibir_vendas(vendas)
    numero_venda = int(input("Digite o número da venda que deseja editar: ")) - 1

    if 0 <= numero_venda < len(vendas):
        novo_valor = float(input("Digite o novo valor da venda: R$"))
        tipo_televisao, _ = vendas[numero_venda].split(',')
        vendas[numero_venda] = f"{tipo_televisao},{novo_valor:.2f}"
        print("Venda editada com sucesso!")
    else:
        print("Número de venda inválido.")

def excluir_vendas(vendas):
    exibir_vendas(vendas)
    numero_venda = int(input("Digite o número da venda que deseja excluir: ")) - 1

    if 0 <= numero_venda < len(vendas):
        del vendas[numero_venda]
        print("Venda excluída com sucesso!")
    else:
        print("Número de venda inválido.")

def salvar_vendas_em_arquivo(vendas):
    nome_arquivo = "vendas.txt"
    with open(nome_arquivo, 'w') as arquivo:
        for venda_info in vendas:
            arquivo.write(f"{venda_info}\n")

def carregar_vendas_do_arquivo():
    vendas = []
    nome_arquivo = "vendas.txt"
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                vendas.append(linha.strip())
    except FileNotFoundError:
        pass  
    return vendas
def iniciocrud():
    vendas = carregar_vendas_do_arquivo()
    while True:
        print("\nOpções:")
        print("1 - Incluir a venda")
        print("2 - Exibir vendas")
        print("3 - Editar vendas")
        print("4 - Excluir vendas")
        print("5 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        
        if opcao == 1:
            incluir_venda(vendas)
        elif opcao == 2:
            exibir_vendas(vendas)
        elif opcao == 3:
            editar_vendas(vendas)
        elif opcao == 4:
            excluir_vendas(vendas)
        elif opcao == 5:
            salvar_vendas_em_arquivo(vendas)
            break
        else:
            print("Opção inválida. Tente novamente.")

    print("Obrigado por usar a Loja TRAKEY!")