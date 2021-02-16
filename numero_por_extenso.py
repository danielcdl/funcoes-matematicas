DECIMAIS = (('décimo', 'décimos'), ('centésimo', 'centésimos'), ('milésimo', 'milésimos'), ('décimo de milésimo', 'décimos de milésimo'),
    ('centésimo de milésimo', 'centésimos de milésimo'), ('milionésimo', 'milionésimos'), ('décimo de milionésimo', 'décimos de milionésimo'),
    ('centésimo de milionésimo', 'centésimos de milionésimo'), ('bilionésimo', 'bilionésimos'), ('décimo de bilionésimo', 'décimos de bilionésimo'), 
    ('centésimo de bilionésimo', 'centésimos de bilionésimo'), ('trilionésimo', 'trilionésimos'), ('quatrilionésimo', 'quatrilionésimos'),
    ('quintilionésimo', 'quintilionésimos'), ('sextilionésimo', 'sextilionésimos'), ('septilionésimo', 'septilionésimos'), ('octilionésimo', 'octilionésimos'),
    ('nonilionésimo', 'nonilionésimos'), ('decilionésimo', 'decilionésimos')
)
UNIDADES = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
DEZENA_ESPECIAL = ('', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
DEZENAS = ('', 'dez', 'vinte', 'trinta', 'quarenta', 'cincoenta', 'sessenta', 'setenta', 'oitenta', 'noventa')
CENTENAS = ('cem', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos','oitocentos', 'novecentos')
MILHAR = (('milhão', 'milhões'), ('bilhão', 'bilhões'), ('trilhão', 'trilhões'), ('quatrilhão', 'quatrilhões'), ('quintilhão', 'quintilhões'),
    ('sextilhão', 'sextilhões'), ('septilhão', 'septilhões'), ('octilhão', 'octilhões'), ('nonilhão', 'nonilhões'), ('decilhão', 'decilhões'),
    ('unodecilhão', 'unodecilhões'), ('duodecilhão', 'duodecilhões'), ('tredecilhão', 'tredecilhões'), ('quatuordecilhão', 'quatuordecilhões'),
    ('quindecilhão', 'quindecilhões'), ('sexdecilhão', 'sexdecilhões'), ('sepdecilhão', 'sepdecilhões'), ('octodecilhão', 'octodecilhões'),
    ('novemdecilhão', 'novemdecilhões')
)
def unidade_dezena_centena(terno):
    numero_extenso = ''
    termos = len(terno)
    digito = terno[0]
    if termos == 3:
        if digito != 0:
            if terno[1:] == [0, 0]:
                if digito == 1:
                    numero_extenso += CENTENAS[0]
                else:
                    numero_extenso += CENTENAS[digito]
            else:
                numero_extenso += CENTENAS[digito] + ' e '
                numero_extenso += unidade_dezena_centena(terno[1:])
        else:
            numero_extenso += unidade_dezena_centena(terno[1:])
    if termos == 2:
        if digito != 0:
                if terno[1] == 0:
                    numero_extenso += DEZENAS[digito]
                elif digito == 1:
                    numero_extenso += DEZENA_ESPECIAL[terno[1]]
                else:
                    numero_extenso += DEZENAS[digito] + ' e ' + unidade_dezena_centena(terno[1:])
        else:
            numero_extenso += unidade_dezena_centena(terno[1:])
    elif termos == 1:
        numero_extenso += UNIDADES[digito]

    return numero_extenso


def milhares(ternos):
    numero_extenso = ''
    termos = len(ternos)
    terno = ternos[0]
    
    if termos >= 3:
        if terno != [0, 0, 0]:
            if terno == [0, 0, 1] or terno == [1]:
                numero_extenso += 'um ' + MILHAR[termos - 3][0]
            else:
                numero_extenso += unidade_dezena_centena(terno) + ' ' + MILHAR[termos - 3][1]

            if ternos[1:] == [[0, 0, 0],[0, 0, 0]]:
                return numero_extenso
            else:
                numero_extenso += ' ' + milhares(ternos[1:])
        else:
            numero_extenso += milhares(ternos[1:])

    if termos == 2:
        if terno != [0, 0, 0]: 
            numero_extenso += unidade_dezena_centena(terno) + ' mil' 
            if ternos[1] == [0, 0, 0]:
                return numero_extenso
            elif ternos[1][0]:
                numero_extenso += ' ' + milhares(ternos[1:])
            else:
                numero_extenso += ' e ' + milhares(ternos[1:])
        else:
            numero_extenso += ' ' + milhares(ternos[1:])
        
    elif termos == 1:
        if terno != [0, 0, 0]:
            numero_extenso += unidade_dezena_centena(terno)

    return numero_extenso



def separar_casas(numero):
    digitos = list(str(numero))
    tamanho = len(digitos)

    
    casa = tamanho % 3
    casas = []
    terno = []
    for i in range(tamanho):
        terno.append(int(digitos[i]))
        if (i + 1) % 3 == casa:
            casas.append(terno)
            terno = []
    return casas

def numero_por_extenso(numero:float):
    numero = str(numero).replace('.',',')
    divisao = numero.split(',')
    if len(divisao) == 1:
        inteiro = int(divisao[0]) 
        decimal = None
    elif len(divisao) == 2:
        inteiro = int(divisao[0])
        decimal = divisao[1]
    else:
        raise ValueError('Número não formatado corretamente')
    
    extenso = milhares(separar_casas(inteiro))
    if decimal != None and int(decimal) != 0:
        while True:
            if decimal[-1] == '0':
                decimal = decimal[:-1]
            else:
                break
        ordem = len(decimal)
        if ordem > 12:
            if ordem > 35:
                raise ValueError("Valor decimal não pode ser escrito pela lib")
            else:
                ordem = 8 + ordem // 3 
    
        if inteiro == 0:
            extenso = ''
        elif inteiro == 1:
            extenso += ' inteiro e '
        else:
            extenso += ' inteiros e '
        if int(decimal) == 1:
            plural = 0
        else:
            plural = 1
        extenso += milhares(separar_casas(decimal)) + ' ' + DECIMAIS[ordem - 1][plural]
        

    return extenso
    
if __name__ == '__main__':
    
    while True:
        try:
            numero = input('Digite um número inteiro: ')
            extenso = numero_por_extenso(numero)
            print(numero, extenso)
            break
        except ValueError:
            print('ERRO!!', end=' ')
