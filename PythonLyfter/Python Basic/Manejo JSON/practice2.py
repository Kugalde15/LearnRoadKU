import json


print(">> Ingresa un nuevo Pokemon <<\n")
name = input("Nombre del Pokemon: ")
lvl = int(input("Nivel del Pokemon: "))
typepoke = input("Tipo de Pokemon: ")
hp = int(input("Vida: "))
attack = int(input("Ataque: "))
defense = int(input("Defensa: "))
sp_atak=int(input("SP. Ataque: "))
sp_defense=int(input("SP. Defense: "))
speed=int(input("Velocidad: "))
new_pokemon={"name" : {
                "english" : name
            },
            "level" : lvl,
            "type" : [
                typepoke
            ],
            "base" : {
                "HP" : hp,
                "Attack" : attack,
                "Defense" : defense,
                "Sp. Attack" : sp_atak,
                "Sp. Defense" : sp_defense,
                "Speed" : speed
            }
}

with open('pokemons.json', 'r',encoding='utf-8') as f:
    list_of_pokes_json = json.load(f)

list_of_pokes_json.append(new_pokemon)

with open('pokemons.json', 'w',encoding='utf-8') as fi:
    json.dump(list_of_pokes_json, fi,indent=4)
print("Pokemon agregado \u2705")