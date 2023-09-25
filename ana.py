def analise_pareto(vendas):
    tipo_vendas = {}
    for venda in vendas:
        tipo_television, valor_venda = venda.split(',')
        valor_venda = float(valor_venda)
        if tipo_television in tipo_vendas:
            tipo_vendas[tipo_television] += valor_venda
        else:
            tipo_vendas[tipo_television] = valor_venda

    # Calcular as vendas totais
    venda_total = sum(valor for valor in tipo_vendas.values())

    # Classificar os tipos de televisão em ordem crescente de vendas
    tipos_ordenados = sorted(tipo_vendas.items(), key=lambda x: x[1])

    porcentagem_contribuicao_acumulada = 0
    tabela_analise_pareto = []
    for tipo, valor in tipos_ordenados:
        porcentagem_contribuicao = (valor / venda_total) * 100
        porcentagem_contribuicao_acumulada += porcentagem_contribuicao
        tabela_analise_pareto.append([tipo, valor, porcentagem_contribuicao, porcentagem_contribuicao_acumulada])

    return tabela_analise_pareto, venda_total