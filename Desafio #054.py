maioridade = 0
menoridade = 0
for c in range(1,8):
    nascimento = int(input('Pessoa nª {}, digite sua data de nascimento: '.format(c)))
    if nascimento > 2000:
        menoridade += 1
    else:
        maioridade += 1
print('Teremos {} pessoa(s) que atingiram a maioridade penal.'.format(maioridade))
print('Teremos {} pessoa(s) que não atingiram a maioridade penal.'.format(menoridade))