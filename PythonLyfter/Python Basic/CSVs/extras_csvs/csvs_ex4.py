import csv


def def_develop():
        user_developer = input('Cual desarrollador desea consultar?: \n==> ')
        user_developer = user_developer.lower()
        read_csv_file('games.csv', user_developer)


def read_csv_file(file_path, dev):
    coun=0
    with open(file_path, 'r' , encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Desarrollador'].lower() == dev:
                print('Coincidencia: ')
                print(f"Nombre: {row['Nombre']} (Clasificacion: {row['Clasificación ESRB']} - Genero: {row['Genero']})")
                print('-'*20)
                coun+=1
    if coun == 0:
        print('No hay coincidencias.')


def main():
    try:
        def_develop()
    except Exception as ex:
        print('Error inesperado: ',ex)


main()