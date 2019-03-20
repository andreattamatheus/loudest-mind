nome = str(input('Digite um frase qualquer: ')).strip().upper()
certo = nome.replace(' ','')
inverso = ''
for c in range(len(certo)-1,-1,-1):
    inverso += certo[c]
if inverso == certo:
    print('É PALINDROMO!')
else:
    print('NÃO É PALÍNDROMO')

