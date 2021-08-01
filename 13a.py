# aula for
n = int(input('Digite um numero: '))
for c in range(n, -1, -1):
    print(c)
print('Fim da Contagem Regressiva')
s=0
for c in range(0,3):
    n=int(input('Digite um número:'))
    s = s+n
print(f'A soma de todos os valores é {s}')