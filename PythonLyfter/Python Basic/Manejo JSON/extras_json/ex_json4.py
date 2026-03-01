import json


def pokemon_by_type():
    electric_type = {'lvl': 0, 'qty': 0}
    fire_type = {'lvl': 0, 'qty': 0}
    water_type = {'lvl': 0, 'qty': 0}
    try:
        with open("pokemons.json", "r", encoding="utf-8") as file:
            poke_py = json.load(file)
        for values in poke_py:
            if "Electric" in values["type"]:
                electric_type['lvl'] += values['level']
                electric_type['qty'] += 1
            if "Fire" in values["type"]:
                fire_type['lvl'] += values['level']
                fire_type['qty'] += 1
            if "Water" in values["type"]:
                water_type['lvl'] += values['level']
                water_type['qty'] += 1
        print(f'Tipo: Electrico \u27A4  promedio de nivel: {round((electric_type['lvl'])/electric_type["qty"],2)}\n')
        print(f'Tipo: Fuego \u27A4  promedio de nivel: {round((fire_type['lvl'])/fire_type["qty"],2)}\n')
        print(f'Tipo: Agua \u27A4  promedio de nivel: {round((water_type['lvl'])/water_type["qty"],2)}\n')
    except FileNotFoundError:
        print("Archivo no encontrado")
        exit()


def main():
    try:
        pokemon_by_type()
    except Exception as ex:
        print("Error inesperado: ", ex)
        exit()


main()