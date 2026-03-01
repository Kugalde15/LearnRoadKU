list = []
for q in range(6):
    i = int(input('Digite su numero: '))
    list.append(i)
print('Tu lista es:' , list)
list[0], list[-1] = list[-1], list[0]
print('Lista modificada: ' , list)