from math import sqrt
a=float(input('Digite o comprimento do cateto oposto: '))
b=float(input('Digite o comprimento do cateto adjacente: '))
c=sqrt(a**2+b**2)
print('O comprimento da hipotenusa é {:0.2f}'.format(c))