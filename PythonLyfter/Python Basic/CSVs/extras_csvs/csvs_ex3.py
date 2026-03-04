import csv


def read_csv_file(file_path):
    acc=0
    adven=0
    sport=0
    rpg=0
    sand=0
    shoot=0
    with open(file_path, 'r' , encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Genero'] == 'Accion':
                acc+=1
            elif row['Genero'] == 'Aventura':
                adven+=1
            elif row['Genero'] == 'Deportes':
                sport+=1
            elif row['Genero'] == 'RPG':
                rpg+=1
            elif row['Genero'] == 'SandBox':
                sand+=1
            elif row['Genero'] == 'Shooter':
                shoot+=1
    print(f'El resultado de la busqueda es: \n{'-'*20}')
    print(f'Accion: {acc}')
    print(f'Aventura: {adven}')
    print(f'Deportes: {sport}')
    print(f'RPG: {rpg}')
    print(f'SandBox: {sand}')
    print(f'Shooters: {shoot}\n{'-'*20}')


def main():
    try:
        read_csv_file('games.csv')
    except Exception as ex:
        print('Error inesperado: ',ex)


main()