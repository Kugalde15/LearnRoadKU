# | Función | Convierte | Desde  | Hacia        |
# | ------- | --------- | ------ | ------------ |
# | loads() | Texto     | JSON   | dict         |
# | dumps() | dict      | Python | Texto JSON   |
# | load()  | Archivo   | JSON   | dict         |
# | dump()  | dict      | Python | Archivo JSON |




# import json

# x = {
#     "name": "John",
#     "age": 30,
#     "married": True,
#     "divorced": False,
#     "children": ("Ann","Billy"),
#     "pets": None,
#     "cars": [
#         {"model": "BMW 230", "mpg": 27.5},
#         {"model": "Ford Edge", "mpg": 24.1}
#     ]
# }

# print(json.dumps(x, indent=1, separators=(". ", " = "), sort_keys=True))

# #json.loads

# import json


# pokes = [
#     {
#         "name": {
#         "english": "Pikachu"
#         },
#         "level": 25,
#         "type": [
#         "Electric"
#         ],
#         "base": {
#         "HP": 35,
#         "Attack": 55,
#         "Defense": 40,
#         "Sp. Attack": 50,
#         "Sp. Defense": 50,
#         "Speed": 90
#         }
#     },
#     {
#         "name": {
#         "english": "Charmander"
#         },
#         "level": 15,
#         "type": [
#         "Fire"
#         ],
#         "base": {
#         "HP": 39,
#         "Attack": 52,
#         "Defense": 43,
#         "Sp. Attack": 60,
#         "Sp. Defense": 50,
#         "Speed": 65
#         }
#     },
#     {
#         "name": {
#         "english": "Squirtle"
#         },
#         "level": 18,
#         "type": [
#         "Water"
#         ],
#         "base": {
#         "HP": 44,
#         "Attack": 48,
#         "Defense": 65,
#         "Sp. Attack": 50,
#         "Sp. Defense": 64,
#         "Speed": 43
#         }
#     }
# ]


# convertir lista (py) a json
# json_pokes = json.dumps(pokes)
# print(type(json_pokes))


#escribir
# with open('pokemons.json', 'w', encoding='utf-8') as f:
#     json.dump(json_pokes,f, indent=4)


#leer
# with open('pokemons.json', 'r', encoding='utf-8') as f:
#     pokks= json.load(f)
#     print(pokks)
#     print(type(pokks))




# import json

# with open('pokemons.json', 'r', encoding='utf-8') as f:
#     contenido = json.load(f)  # esto carga el string

# data_real = json.loads(contenido)  # convierte el string en lista real

# with open('pokemons.json', 'w', encoding='utf-8') as f:
#     json.dump(data_real, f, indent=4)

# print("Archivo reparado ✅")








e=0
print(e, e+10)
e=1

print(e)