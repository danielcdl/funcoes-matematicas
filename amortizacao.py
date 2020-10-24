def amortizar(p: float, n: int, i: float):
    """
    :param p: Valor da divida
    :param n: Tempo em meses
    :param i: Taxa de juros(composto) mensal
    :return: Valor da parcela
    """

    pgto = p / n + p * i
    return pgto


linha = [1, 500000.00, 7500.00, 5000.00, 2500.00, 45000.00]
numero, saldo_inicial, prestacao, amortizacao, juros, saldo_final = linha
print(
    f'{numero:^6}         {saldo_inicial:>13,.2f}           {prestacao:>9,.2f}                {amortizacao:>11,.2f}           {juros:>9,.2f}        {saldo_final:>11,.2f}')
# '  1        50,000.00    7,500.00       5,000.00     2500.00     45,000.00
