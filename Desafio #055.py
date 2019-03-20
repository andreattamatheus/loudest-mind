maior = 0
menor = 0
for peso in range(1,6):
    kilos = float(input('{}ª - Valor em Kilogramas: '.format(peso)))
    if peso == 1:
        maior = kilos
        menor = kilos
    else:
        if kilos > maior:
            maior = kilos
        if kilos < menor:
            menor = kilos
print('O maior valor é {}Kg'.format(maior))
print('O menor valor é {}Kg'.format(menor))