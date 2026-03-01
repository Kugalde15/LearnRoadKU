# Cree un programa que muestre el valor más pequeño de una list sin usar min().
# Use una variable para comparar uno a uno.

list = []
for n in range (7):
    q = int(input('Digite un valor: '))
    list.append(q)
firts = list[1]
for n in list:
    if n < firts:
        firts = n

print( 'Tu lista: ', list)
print('El numero menor es: ', firts)