media = 0
mulheres = 0
velho = 0
pessoa = ''
for pessoas in range(1,5):
    nome = str(input('{}ª - Digite seu nome: '.format(pessoas)))
    idade = int(input('{}ª - Digite a sua idade: '.format(pessoas)))
    sexo = str(input('{}ª - Digite seu sexo: '.format(pessoas))).upper()
    media = media + idade                                    #Primeira Condição
    if pessoas == 1:
        velho = idade
        pessoa = nome
    else:
        if idade > velho:
         velho = idade
        pessoa = nome

    if sexo == 'FEMININO':                                   #Terceira Condição
        if idade < 20:
            mulheres += 1
    print('='*30)

print('A média de idade é de {} anos.'.format(int(media/4)))
print('{} mulheres tem menos de 20 anos.'.format(mulheres))
print('A pessoa mais velha é {}.'.format(pessoa))

#print('O mais velho é {}'.format(nome))