# funções
def mensagem(msg):   # função com parametro
    print('-='*15)
    print(msg)
    print('-='*15)


def soma(a, b):    # função com parametros sem desempacotar (limitado)
    s = a+b
    print(f'A soma de {a} + {b} é igual a {s}')


def soma2(* num):   # empacotamento de parametros
    s = 0
    for n in num:
        s += n
    print(f'A soma dos valores é {s}')


def contador(*num):
    print(len(num))


def dobra(lista):   # def com listas - altera diretamente
    c = 0
    while c < len(lista):
        lista[c] *= 2
        c += 1


mensagem('Começo do programa teste de funções')
soma(1, 3)
soma2(1, 3, 5, 6, 1)
contador(4, 5, 6, 8, 9)
lista = [5, 6, 8, 9]
dobra(lista)
print(lista)
