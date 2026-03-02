# Cree un programa que use una lista para eliminar keys de un diccionario.
# Ejemplos:
# list_of_keys = [’access_level’, ‘age’]
# employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}
# → {’name’: ‘John’, 'email’: ‘john@ecorp.com’}

my_son = {
    'name' : input('Nombre: '),
    'age' : int(input('Edad: ')),
    'sex' : input('sexo: '),
    'type' : input('tipo de sangre: ')
}

print(my_son)

del_keys = ['type' , 'sex']
for pop in del_keys:
    my_son.pop(pop)
print(my_son)