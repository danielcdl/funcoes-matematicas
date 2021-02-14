def mudar_base(n:int, base:int):
    """
    Funcão que faz mudança de base se um número
    :param n:int
    :param base:int inteiro positivo

    :return int numero na base selecionada
    """

    dividendo = n
    conversao = 0
    indice = 1
    while dividendo != 0:
        conversao += (dividendo % base) * indice
        indice *= 10
        dividendo = dividendo // base
    return conversao