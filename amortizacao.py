def imprimir_tabela_sac(dados,
                        cabecalho=(
                                'periodo',
                                'saldo inicial',
                                'juros calc.',
                                'saldo após juros',
                                'pgto', 'amortizado',
                                'juros pago',
                                'saldo final'
                        ),
                        lista_espacos=(1, 1, 1, 1, 1, 1, 1, 1)):
                        #espacos=(9, 14, 12, 18, 6, 12, 12, 12)):


    # depois criar uma exceção caso cabeçalho e espaços tenham a quantidade de itens diferentes
    espacos = []
    for celula, espaco in zip(cabecalho, lista_espacos):
        if len(celula) + 2 > espaco:
            espacos.append(len(celula) + 2)
        else:
            espacos.append(espaco)

    # cabeçalho
    divisa_grossa = ' ' + '='*(sum(espacos) + len(espacos) + 1)
    print(divisa_grossa)
    print('||', end='')
    for celula, espaco in zip(cabecalho, espacos):
        escape = int((espaco - len(celula))/2) * ' '
        print(escape + celula + escape, end='|')
    print('|')
    print(divisa_grossa)

    # corpo
    for linha in dados:
        print('||', end='')
        for celula, espaco in zip(linha, espacos):
            dado = str(linha[celula])
            escape = int((espaco - len(dado)) / 2) * ' '
            print(escape + dado + escape, end='|')
        print('|')

    # rodapé
    print(divisa_grossa)


def sac(entradas=False):
    n = 4
    divida = 800
    taxa = 0.1
    if entradas:
        while True:
            try:
                n = int(input('Digite a quantidade de meses: '))
                break
            except ValueError:
                print('Erro! Digite um valor inteiro')

        while True:
            try:
                divida = float(input('Digite o valor da divida: ').replace('.', '').replace(',', '.'))
                break
            except ValueError:
                print('Erro! Digite um valor real')

        while True:
            try:
                taxa = float(input('Digite o valor da taxa: ').replace('.', '').replace(',', '.'))
                break
            except ValueError:
                print('Erro! Digite um valor real')

    amortizado = divida / n
    dados = []
    for n in range(1, n + 1):
        juros = divida * taxa
        saldo_apos_juros = divida + juros
        pgto = amortizado + juros
        saldo_final = saldo_apos_juros - pgto
        dados.append({'n': n,
                      's_ini': divida,
                      'juros': juros,
                      's_apos_juros': saldo_apos_juros,
                      'pgto': pgto,
                      'amortizado': amortizado,
                      'juros_pago': juros,
                      'saldo_final': saldo_final
                      })
        divida = saldo_final

    imprimir_tabela_sac(dados)

sac()
