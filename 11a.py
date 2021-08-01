#primeira maneira, durante o print
print('\033[4;34;47mOlá, mundo!\033[m')
nome = 'Fernanda'
#segunda maneira, na formatação final
print('Olá, seja bem vindo, {}{}{}'.format('\033[4;34;47m',nome,'\033[m'))
#terceira maneira, cores predefinidas em uma variável
cores = {'limpa':'\033[m','azul':'\033[34m','amarelo':'\033[33m','pretoebranco':'\033[7;30m'}
print('Seja muito bem vindo, {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))
