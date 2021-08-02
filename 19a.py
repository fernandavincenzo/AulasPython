#dicionários

dados2 = {'nome': 'Pedro', 'idade': 25}
print(dados2['nome'])
print(dados2['idade'])
dados2['sexo'] = 'M'   #n necessita append
print(dados2['sexo'])
del dados2['idade']
filmes = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(filmes.values())  #valores (star wars, 1977, george lucas)
print(filmes.keys())    #chaves(nome dos valores)
print(filmes.items())   #itens (todos os elementos)

for k, v in filmes.items():   #para cada chave, valores
    print(f'O {k} do filme é {v}')

locadora = [filmes]
print(locadora[0]['ano'])