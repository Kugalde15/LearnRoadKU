def open_and_print_file_per_line(path):
	cellphones = ''
	try:
		with open(path) as file:
			for line in file.readlines():
				cellphones+=line
		cellphones = cellphones.upper()
	except FileNotFoundError:
		print('El archivo no existe')
	return cellphones


def write_text_to_file(file_path, str):
	with open(file_path, 'w') as file:
		for line in str:
			file.write(line)


def main():
	try:
		write_text_to_file("upper_cell.txt", open_and_print_file_per_line('cellphones.txt'))
	except Exception as ex:
		print(f'Error inesperdo: {ex}')
	exit()


main()