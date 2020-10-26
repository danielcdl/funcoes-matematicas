from datetime import datetime
from random import randrange  # retorna um numero aleatorio


def imprimir_tabela(lista_dados, cabecalho, lista_espacos):
    # depois criar uma exceção caso cabeçalho e espaços tenham a quantidade de itens diferentes
    espacos = []
    for celula, espaco in zip(cabecalho, lista_espacos):
        if len(celula) + 2 > espaco:
            espacos.append(len(celula) + 2)
        else:
            espacos.append(espaco)

    # cabeçalho
    divisa_grossa = ' ' + '=' * (sum(espacos) + len(espacos) + 1)
    print(divisa_grossa)
    print('||', end='')
    for celula, espaco in zip(cabecalho, espacos):
        escape = int((espaco - len(celula)) / 2) * ' '
        print(escape + celula + escape, end='|')
    print('|')
    print(divisa_grossa)

    # corpo
    for linha in lista_dados:
        print('||', end='')
        for i, espaco in zip(range(len(linha)), espacos):
            dado = str(linha[i])
            escape = int((espaco - len(dado)) / 2) * ' '
            print(escape + dado + escape, end='|')
        print('|')

    # rodapé
    print(divisa_grossa)


def miller_rabin(n_testado, t=1000):  # Realiza o Teste de Miller-Rabin t vezes para o numero n
    if t > n_testado - 3:  # o numero de tentativas nao pode exceder n-3
        t = n_testado - 3
    s = 0
    m = n_testado - 1
    div = divmod(m, 2)
    while div[1] == 0:  # encontra r e s de n-1= (2^s)m
        m = div[0]
        div = divmod(m, 2)
        s += 1

    r = []  # será a lista com os os restos da divisao sucessiva de m por 2
    while m > 0:  # encontra os r_1 de da conversao para base 2
        divisao = divmod(m, 2)
        m = divisao[0]  # faz m igual ao quaciente da divisão de m por 2
        r.append(divisao[1])  # adiciona m mod 2 na lista r

    bases = []
    j = 0
    while j < t:  # cria uma lista com t numeros inteiros distintos petencentes ao intervalo  [2,n-1[
        a_i = randrange(2, n_testado - 1)
        if a_i not in bases:
            bases.append(a_i)
            j += 1
    for a in bases:
        e = a  # para nao alterar o valor de a, usei outra variavel com seu valor
        y = a  # como m é impar, r[0] sempre é 1, sendo descencessario fazer e**r[0]
        for expoente in r[1:]:  # calcula a^k mod n pelo algoritmo da reducao de custo de a^c mod n
            e = e * e % n_testado  # é mais rápido calcular uma multiplicação do que uma potencia
            if expoente == 1:
                y = y * e % n_testado
        if y != 1 and y != n_testado - 1:
            i = 1
            while i <= s - 1 and y != n_testado - 1:
                y = y * y % n_testado
                if y == 1:
                    return "composto"
                i += 1
            if y != n_testado - 1:
                return "composto"
    return "primo"  # se ao final de t testes, n não for como composto, dizemos que ele é primo


limites = ('10',
           '50',
           '100',
           '150',
           '1.000',
           '1.500',
           '10.000',
           '10.500',
           '100.000',
           '150.000',
           '1.000.000',
           '1.500.000',
           '10.000.000',
           '10.500.000',
           '100.000.000',
           '100.500.000',
           '1.000.000.000',
           '1.500.000.000',
           '10.000.000.000',
           '10.500.000.000',
           '100.000.000.000',
           '100.500.000.000',
           '1.000.000.000.000',
           '1.500.000.000.000',
           '1.000.000.000.000.000',
           '1.500.000.000.000.000',
           '1.000.000.000.000.000.000',
           '1.500.000.000.000.000.000',
           '1.000.000.000.000.000.000.000',
           '1.000.000.000.000.000.000.000.000',
           )
print(len(limites))
dados = []
for numero in limites:
    n = int(numero.replace('.', ''))
    if n % 2 == 0:
        n = n - 1

    tempo_inicio = datetime.now()
    while True:
        resultado = miller_rabin(n)
        if resultado == 'primo':
            tempo_fim = datetime.now()
            tempo_gasto = tempo_fim - tempo_inicio
            break
        else:
            n -= 2
    dados.append((numero, n, tempo_gasto))

imprimir_tabela(dados, ('Limite', 'Último primo', 'Tempo'), (35, 26, 16))
