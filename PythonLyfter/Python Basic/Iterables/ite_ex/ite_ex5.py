# Cree un programa que le pida al usuario ingresar 5 palabras. 
# Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras.

words = []
for pala in range(5):
    q = str(input('Ingrese su palabra: '))
    words.append(q)
plus4 = []
for q in words:
    if len(q) > 4:
        plus4.append (q)

print('Sus palabras son: ', words)
print('Las palabras de mas de 4 letras son: ',plus4)