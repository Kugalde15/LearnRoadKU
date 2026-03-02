print('~~~ Number 30 ~~~')

num1 = int(input('Digite su 1er numero: '))
num2 = int(input('Digite su 2do numero: '))
num3 = int(input('Digite su 3er numero: '))

if num1 == 30 or num2 == 30 or num3 == 30 :
    print('correcto')
elif num1 + num2 + num3 == 30 :
    print('correcto')
else: 
    print('incorrecto')