# funções - parte 2

# interactive help (console python - help() )
# ou: help(input)

# docstring:
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela:
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = 0
    for c in range(i, f+1, p):
        print(c, end=' ')
    print('Fim')


help(contador)


# parâmetros opcionais:
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


# retornando valores:
n1 = somar(8, 4)
n2 = somar()
print(f'Os resultados das somas foram {n1} e {n2}')

# escopo de variáveis
def teste():
    n = 8  # duas variáveis n, uma global e outra local
    x = 8
    print(f'Na função teste n = {n}')
    print(f'Na função teste x = {x}')


n = 2
print(f'No programa principal, n = {n}')   # funciona no princ e na def pq foi declrada num escopo global
# print(f'No programa principal x = {x}')   ñ vai funcionar pq a váriavel está no escopo local (função)
teste()

