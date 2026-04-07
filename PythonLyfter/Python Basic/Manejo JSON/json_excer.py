import json


def create_new_pokemon():
    name = input("Nombre del Pokemon: ")
    typepoke1 = input("Tipo del Pokemon: ")
    print('Desea agregar otro tipo de elemento?: Y / [Any Key] ')
    opc = input('\u27A4  ').upper()
    if opc == 'Y':
        typepoke2 = input("Segundo tipo del Pokemon: ")
    lvl = get_stats('Nivel', "Nivel del Pokemon: ")
    hp = get_stats('HP', "Vida: ")
    attack = get_stats('Ataque', "Ataque: ")
    defense = get_stats('Defensa', "Defensa: ")
    sp_atak = get_stats('SP. Ataque',"SP. Ataque: ")
    sp_defense = get_stats('SP. Defense', "SP. Defense: ")
    speed = get_stats('Velocidad', "Velocidad: ")

    new_pokemon = {
        "name": {"english": name},
        "level": lvl,
        "type": [typepoke1,typepoke2],
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_atak,
            "Sp. Defense": sp_defense,
            "Speed": speed
                }
    }
    read_extract_and_add(new_pokemon)


def get_stats(stat_name, show_str):
    while True:
        try:
            stats = int(input(show_str))
            break
        except ValueError:
            print(f"El {stat_name} debe ser un numero\n")
    return stats

def read_extract_and_add(new_item):
    try:
        with open('pokemons.json', 'r',encoding='utf-8') as f:
            list_of_pokes_json = json.load(f)

        list_of_pokes_json.append(new_item)

        with open('pokemons.json', 'w',encoding='utf-8') as fi:
            json.dump(list_of_pokes_json, fi,indent=4)
        print("Pokemon agregado \u2705\n")
        another_pokemon()
    except FileNotFoundError:
        print("❌ Archivo no encontrado, verifique la informacion")
        exit()
    except ValueError:
        print("\n❌ Arvhico vacio, sin datos para leer\n")
        exit()


def another_pokemon():
    print("Desea agregar otro Pokemon?: ")
    try:
        opc = input('Y / N ? \n\u27A4  ').upper()
        if opc == 'Y':
            print("Agregue la informacion del nuevo Pokemon \n")
            main()
        elif opc == 'N':
            exit()
        else:
            raise ValueError
    except ValueError:
        print("❌ Digite una tecla valida (Y/N), intente nuevamente\n")
        another_pokemon()



def main():
    try:
        create_new_pokemon()
    except Exception as ex:
        print(f"❌ Error inesperado: {ex}")


main()
