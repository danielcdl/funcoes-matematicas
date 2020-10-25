base = {1:('zero', 'um', 'dois','três','quatro','cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
                    'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove'),
        2:'vinte', 3:'trinta',4:'quarenta', 5:'cincoeta', 6:'sesenta', 7:'setenta', 8:'oitenta', 9:'noventa',
        'centena': ('cem', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos',
                   'oitocentos', 'novecentos'),
        'unidade_milhar':('mil',),
        'milhar': ('milhão', 'milhões', 'bilhão', 'bilhões')
       }


def numero_por_extenso(numero):
    digitos = list(str(numero))
    tamanho = len(digitos)
    for i in range(tamanho):
        digitos[i] = int(digitos[i])

    n_extenso = ''
    for digito, i in zip(digitos, range(tamanho+1)):
        if i == tamanho-2:
            if digito < 2:
                n_extenso += base[1][int(digitos[i]*10 + digitos[i+1])]
                break
            else:
                n_extenso += base[digito]
                if digitos[i+1] != 0:
                    n_extenso += ' e '
                else:
                    break

        elif i == tamanho-1:
            n_extenso += base[1][digitos[i]]

    print(n_extenso)

numero = 9
while numero < 100:
    try:
        #numero = int(input('Digite um número inteiro: '))
        numero_por_extenso(numero)
        numero += 10
    except ValueError:
        print('Digite um número inteiro')
