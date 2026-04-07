import csv


def def_user_games():
    list_of_user_games = []
    while True:
        try:
            qty_games = int(input('Cuantos juegos desea agregar?: '))
            for val in range(qty_games):
                    name = input(f'{val+1}- Nombre del Juego: \n==> ')
                    gender = input(f'{val+1}- Genero del juego: \n==> ')
                    develop = input(f'{val+1}- Desarrollador: \n==> ')
                    class_esrb = input(f'{val+1}- Clasificación ESRB: \n==> ')
                    game = {
                    'Nombre':name,
                    'Genero':gender,
                    'Desarrollador':develop,
                    'Clasificación ESRB':class_esrb,
                    }
                    list_of_user_games.append(game)
                    header = (
                'Nombre',
                'Genero',
                'Desarrollador',
                'Clasificación ESRB'
            )
            write_csv_file('games_2.0.csv', list_of_user_games, header)
            break
        except ValueError:
            print('Dato invalido, debe ser numero')


def write_csv_file(file_path, data, header):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, header, delimiter='\t')
        writer.writeheader()
        writer.writerows(data)


def main():
    try:
        def_user_games()
    except Exception as ex:
        print(f'Error inesperado: {ex}')
        exit()


main()