#personalização de string
f: str = '    Fernanda Vincenzo     '
print(len(f))
print(f[:8])
print(f[9:])
print(f.count('o'))
print(f.upper())
print(f.strip())
print(f.split())
print(f.replace('Vincenzo', 'Kruger').strip())
print(f.find('Vincenzo'))
print('Fernanda' in f)
