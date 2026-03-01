nombre = input('Cual es su nombre: ')
apellido = input('Cual es su apellido: ')
edad = int(input('Cual es su edad: '))

if edad < 2 :
    print('Eres un bebe')
elif edad < 5 :
    print('Eres un nino')
elif edad < 12:
    print('Eres preadolescente')
elif edad < 18 : 
    print('Eres un adolecente')
elif edad < 21 :
    print('Eres un adulto joven')
elif edad < 65:
    print('Eres un adulto')
else: 
    print('Eres un adulto mayor')
print(nombre , apellido)