#apenas if/else:
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Agora, digite sua segunda nota: '))
m = (n1+n2)/2
print(f'Sua média foi {m:.2f}')
if m>=6.0:
    print('Sua média foi muito boa, parabéns!!')
else:
    print('Que pena...Sua média não foi muito boa :(')
    