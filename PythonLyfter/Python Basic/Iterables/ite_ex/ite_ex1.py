# Cree un programa que cuente cuántas veces aparece un número específico en una lista. 
# Pida al usuario una lista de números y otro número a buscar

lista = []
print('Digite 7 numeros')
for n in range (7):
  i = int(input('Digite un numero: '))
  lista.append(i)
print(lista)
num_sch = int(input('Numero a buscar: '))
numm = 0
for q in lista:
  if q == num_sch:
    numm += 1
print(f'El numero {num_sch} aparece {numm} veces')