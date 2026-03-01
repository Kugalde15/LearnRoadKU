import json


def read_json():
   try:
      with open("pokemons.json", "r", encoding="utf-8") as file:
         poke_py = json.load(file)
   except FileNotFoundError:
      print("Archivo no encontrado\n")
   return poke_py


def find_type_pokemon():
   while True:
      user_type = input(f"\nQue tipo de Pokemon desea buscar?[Fuego, Agua o Eléctrico]: \n\u27A4  ").lower()
      user_type=translate_en_to_es(user_type)
      if user_type:
         break
   print(f'\nPokemones tipo {user_type.capitalize()} son:')
   poke_py = read_json()
   for vals in poke_py:
      types_of_pokes = []
      tpe = vals["type"]
      for tpes in tpe:
         tpes=tpes.lower()
         types_of_pokes.append(tpes)
      if user_type in types_of_pokes:
         print(vals["name"]["english"])
   print()
   exit()


def translate_en_to_es(user_type):
   if user_type.lower() in ("fire", "fuego"):
      return "fire"
   elif user_type.lower() in ("water", "agua"):
      return "water"
   elif user_type.lower() in ("electrico", "electric", "eléctrico"):
      return "electric"
   print("El tipo de pokemon no se encuentra en la data\n")
   return None


def main():
   try:
      find_type_pokemon()
   except Exception as ex:
      print("Error inesperado: ", ex)
      exit()


main()