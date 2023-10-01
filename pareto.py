from crud import iniciocrud,incluir_venda,exibir_vendas,editar_vendas,excluir_vendas,salvar_vendas_em_arquivo,carregar_vendas_do_arquivo
from ana import analise_pareto
print("Bem-vindo à Loja TRAKEY - Revendedora de Televisões\n*Programa realizado por: Larissa Matsuda, Roger Santos e Suellen Donato* ")

while True:
    print("\nOpções:")
    print("1 - Inclusão de dados")
    print("2 - Análise de Pareto")
    print("5 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        iniciocrud()
    elif opcao == 2:
        vendas = carregar_vendas_do_arquivo()
        tabela_analise_pareto, venda_total = analise_pareto(vendas)
        print("\nTabela de Análise de Pareto (Ordem Crescente):")
        print("{:<15} {:<15} {:<15} {:<15}".format("Tipo", "Vendas Totais", "% Contribuição", "% Contribuição Acumulada"))
        for linha in tabela_analise_pareto:
            print("{:<15} {:<15.2f} {:<15.2f} {:<15.2f}".format(linha[0], linha[1], linha[2], linha[3]))
        print("Venda Total:    {:.2f}".format(venda_total))
    elif opcao == 5:
        break
    else:
        print("Opção inválida. Tente novamente.")

print("Obrigado por usar a Loja TRAKEY!")