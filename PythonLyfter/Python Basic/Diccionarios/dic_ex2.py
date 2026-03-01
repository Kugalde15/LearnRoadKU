# Cree un programa que cree un diccionario usando dos listas del mismo tamaño, 
# usando una para sus keys, y la otra para sus values.
# Ejemplos:
# list_a = [’first_name’, ‘last_name’, ‘role’]
# list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]
# → {’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}

person_1 = [
    'first_name', 
    'last_name' , 
    'role',
    'schedule',
    ]

values_1 = [
    'Keylor',
    'Ugalde',
    'Tecnico',
    '7 a 5',
]

dctny = {}

for val in range(len(person_1)) :
    dctny[person_1[val]] = values_1[val]

print(dctny)