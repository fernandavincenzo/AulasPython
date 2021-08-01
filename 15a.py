# Aula de breaks
soma = c = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    c += 1
print(f'A soma dos {c} valores é de {soma}')  # fstrings
