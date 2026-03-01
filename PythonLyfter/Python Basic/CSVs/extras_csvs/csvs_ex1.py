import csv


def read_csv_file(file_path):
    with open(file_path, 'r' , encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for key, value in row.items():
                print(f'{key} : {value}')
            print()
read_csv_file('games.csv')