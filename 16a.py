# tuplas - variáveis compostas
lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
print(lanche[-1])
print('Os itens disponívei em nosso cardápio são:')

for item in lanche:
    print(item)

for c in range(0, len(lanche)):  #len = 4 espaços, então o range vai de (0, 4), mostrando todos pois para no 3
    print(f'{lanche[c]} na posição {c}')  #mostra o item e a posicao, maneira 1

for posicao, item in enumerate(lanche):  ##mostra o item e a posicao, maneira 2
    print(f'{item} na posicao {posicao}')

print(sorted(lanche))  #Colocar ordem alfabética

a = 1, 5, 6
b = 2, 4, 7
c = a + b  #união dos conjuntos tuplas
print(sorted(c))
print(c.index(1))
