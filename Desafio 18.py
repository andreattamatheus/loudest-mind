import math
a=float(input('Digite um ângulo qualquer: '))
se=math.sin(math.radians(a))
co=math.cos(math.radians(a))
tg=math.tan(math.radians(a))

print('Os valores do ângulo {} são respectivamente: \nSeno {:0.2f} \nCosseno {:0.2f}  \nTangente {:0.2f}'.format(a,se,co,tg))