num = []
num.append(6)
num.append(4)
num.append(45)
print(num)
for cont in range(0,3):
    num.append(int(input('Digite um valor para ser adicionado na lista: ')))
print(num)
for c, v in enumerate(num):
    print(f'Na posição {c} encontrei o valor {v}')
a = [13,2,3,4]
b = a
b[2] = 8
print(a, b)   #Quando duas listas são igualadas, há uma conexão entre elas e muda as duas
b = a[:]  #Dessa forma se cria uma cópia e pode alterar apenas a lista b, sem mudar a A