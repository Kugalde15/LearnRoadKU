import json


def read_and_show_inf():
   files = input(f"Nombre del archivo que desea consultar: \n\u27A4  ")+".json"
   try:
      with open(files, "r", encoding="utf-8") as file:
         poke_py = json.load(file)
      #print(f'{type(poke_py)}, \n {poke_py}')
      for vals in poke_py:
         print(f'Nombre: {vals['name']['english']}\nNivel: {vals['level']}\nTipo: {vals['type']}')
         print('-'*20)
   except FileNotFoundError:
      print("Archivo no , digite uno valido: \n")
      return main()


def main():
   try:
            read_and_show_inf()
   except Exception as ex:
      print("Error inesperado: ", ex)
      exit()


main()