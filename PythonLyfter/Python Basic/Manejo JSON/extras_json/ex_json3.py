import json


def pokemon_stats():
    try:
        with open("pokemons.json", "r", encoding="utf-8") as file:
            poke_py = json.load(file)
            for vals in poke_py:
                print(
                f"Nombre: {vals['name']['english']}\n"
                f"HP: {vals['base']['HP']}\n"
                f"Ataque: {vals['base']['Attack']}\n"
                f"Defensa: {vals['base']['Defense']}\n"
                f"Sp. Ataque: {vals['base']['Sp. Attack']}\n"
                f"Sp. Defensa: {vals['base']['Sp. Defense']}\n"
                f"Velocidad: {vals['base']['Speed']}"
                )
                print("-" * 20)
    except FileNotFoundError:
        print("Archivo no encontrado")
        exit()


def main():
    try:
        pokemon_stats()
    except Exception as ex:
        print("Error inesperado: ", ex)
        exit()


main()