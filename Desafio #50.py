soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite {}ª valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont = c+1
print('Foi informado {} valore(s) pares com somatório igual a {}'.format(cont,soma))