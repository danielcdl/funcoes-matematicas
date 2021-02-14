def mudar_base(n:int, base:int) -> list:
    """
    Funcão que faz mudança de base se um número
    :param n:int
    :param base:int inteiro positivo

    :return list lista de digitos em ordem inversa da base selecionada
    """

    dividendo = n
    conversao = []
    while dividendo != 0:
        resto = dividendo % base
        conversao.append(resto)
        dividendo = dividendo // base
    return conversao

def modulo_n(a:int, n:int, k:int=1):
    """
    Função que calcula (a elevado a k) módulo n, ou seja, a^k mod n

    :param a:int 
    :param n:int
    :param k:int

    :return int a^k mod n
    """

    expoentes_base2 = mudar_base(k, 2)
    exp = a % n
    a_pow_k_mod_n = 1
    for expoente in expoentes_base2:
        if expoente == 1:
            a_pow_k_mod_n = (a_pow_k_mod_n * exp) % n
        exp = int(exp * exp) % n
    
    return a_pow_k_mod_n
