def open_and_print_file_per_line(path):
	my_string = ''
	try:
		with open(path) as file:
			print(f'El archivo contiene {len(file.read())} palabras')
	except FileNotFoundError:
		print('El archivo no existe')
	return my_string


def main():
	try:
		open_and_print_file_per_line('history.txt')
	except Exception as ex:
		print(f'Error inesperdo: {ex}')
	exit()


main()