filmes = []
filme = {}
for c in range(0,3):
    filme['nome'] = input('Nome do Filme: ')
    filme['ano'] = int(input('Ano do Filme: '))
    filme['diretor'] = input('Diretor do Filme: ')
    filmes.append(filme.copy())

for f in filmes:
    for k, v in f.items():
        print(f'O {k} do filme é {v}')

