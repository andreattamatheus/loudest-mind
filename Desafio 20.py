import random
a=str(input('Qual o nome do primeiro aluno '))
b=str(input('Qual o nome do segundo aluno '))
c=str(input('Qual o nome do terceiro aluno '))
d=str(input('Qual o nome do quarto aluno '))
list = [a,b,c,d]
random.shuffle (list)
print('A ordem de apresentação será:')
print(list)