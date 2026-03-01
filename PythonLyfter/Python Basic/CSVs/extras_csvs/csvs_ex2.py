import csv


def def_class():
    try:
        class_esrb = input('Cual es la Clasificación ESRB que desea?: \n==> ')
        class_esrb = class_esrb.upper()
        if class_esrb in ['M' , 'E10' , 'E' , 'T' , 'AO']:
            read_csv_file('games.csv', class_esrb)
        else:
            raise ValueError
    except ValueError:
        print('Clasificacion incorrecta, intente nuevamente \n')
        main()


def read_csv_file(file_path, clas):
    coun=0
    with open(file_path, 'r' , encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Clasificación ESRB'] == clas:
                coun+=1
                print(f'Juego #{coun} encontrado: \n')
                for key, value in row.items():
                    print(f'{key} : {value}')
                print()
    if coun == 0:
        print('No se encontraron juegos.')


def main():
    try:
        def_class()
    except Exception as ex:
        print('Error inesperado: ',ex)


main()