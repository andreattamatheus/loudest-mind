razao = int(input('Digite uma razão para uma PA: '))
termo = int(input('Digite o primeiro termo da PA: '))
print ('A razão dessa PA é de {}.'.format(razao))
print('Os 10 primeiros termos são:')
for termo in range (termo,(termo+(10-1)*razao),razao):
    soma = termo + razao
    print('{}'.format(soma), end=' -> ')
print('Acabou')