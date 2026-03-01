# Cree un programa que reciba una lista de números y calcule el promedio de los valores, 
# luego cree una nueva lista con solo los valores mayores al promedio

lista = []
for n in range(7):
    q = int(input('Digite un valor: '))
    lista.append(q)
mayores = []
suma = 0
for a in lista:
    suma = suma + a
promedio = suma / 7
for n in lista :
    if n > promedio:
        mayores.append(n)
print('Tu lista:', lista)
print('Promedio: ',promedio)
print(f'Los mayores a {promedio} son: {mayores}')