# Cree un programa que verifique si todos los elementos de una lista son positivos
# Restricciones:
# No use funciones como all()

grados = [0, -1, 2, 34, -33, 49, 97, -77]

for q in grados:
    if q < 0 : 
        print('Negativo "-" ')
    else:
        print('Positivo "+"')