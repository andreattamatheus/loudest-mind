frase = str(input('Digite alguma frase: ')).upper().strip()
a = frase.count("A")
p = frase.find('A')
u = frase.rfind('A')
tudo = len(frase)
print('Número de caracteres',tudo)
print('Quantas vezes a letra "a" aparece: {}'.format(a+1))
print('Em que posição a letra "a" aparece a primeira vez: {}'.format(p+1))
print('Em que posição a letra "a" aparece a última vez: {}'.format(u+1))