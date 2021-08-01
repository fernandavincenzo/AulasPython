#condições aninhadas if/elif
nome = str(input('Qual é o seu nome? '))
if nome == 'Fernanda':
    print('Que lindo nome você tem!')
elif nome == 'João':
    print('O seu nome é igual ao do meu pai!')
elif nome == 'Carla':
    print('O seu nome é igual ao da minha mãe!')
else:
    print('Que nome normal...')
print(f'Tenha um bom dia, {nome}!')
