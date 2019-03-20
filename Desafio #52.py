num = int(input('Digite um número: '))
cont = 0
for c in range (1,num+1):
    if num % c == 0:
        print('\033[1;31m{}\033[m'.format(c),end=' ')
        cont += 1

    else:
        print('{}'.format(c),end=' ')

print('\nO número {} foi divisível {} vezes.'.format(num,cont))
if cont > 2:
    print('Esse número não é primo por ser divisível por mais de 2 vezes.'.format(cont))
elif cont == 1:
    print('Esse número é primo devido ser divisível apenas por ele mesmo.'.format(cont))
else:
    print('Esse número é primo devido ser divisível apenas por 1 e ele mesmo.'.format(cont))