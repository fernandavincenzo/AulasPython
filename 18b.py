pessoal = [['Joaquina', 19], ['Fernanda', 15], ['Joao', 57], ['Luiz', 23]]
for p in pessoal:
    print(f'{p[0]} tem {p[1]} anos de idade')

gente = list()
dados = list()
for c in range(0,3):
    dados.append(input('Nome: '))
    dados.append(int(input('Idade: ')))
    gente.append(dados[:])
    dados.clear()
maiores = menores = 0
for p in gente:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        maiores += 1
    else:
        print(f'{p[0]} é menor de idade')
        menores += 1
print(f'Temos {maiores} pessoas maiores de idade e {menores} menores de idade')