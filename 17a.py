# listas:
lista = ['suco', 'hamburguer', 'pizza', 123]
lista.append('Cookie')   #adciona no final da lista
lista.insert(0, 'cachorro quente')  #Adiciona no 0
print(len(lista))
del lista[2]   #apaga forma 1
lista.pop()   #apaga forma 2 - elemento inserido pelo indice ou o último (parenteses sozinhos)
if 'pizza' in lista:
    lista.remove('pizza')   #apaga forma 3 - pelo nome do elemento
print(lista)
valores = list(range(4,11))   #cria com numeros 4 até 10
print(valores)
valores2 = [2, 3, 5, 9, 2, 3, 6]
valores2.sort()  #bota em ordem
valores2.sort(reverse=True)  #bota em ordem decrescente
print(valores2)
