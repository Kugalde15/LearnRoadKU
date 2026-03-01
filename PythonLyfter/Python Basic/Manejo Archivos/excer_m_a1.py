def open_and_print_file_per_line(path):
	my_songs = []
	try:
		with open(path) as file:
			for line in file.readlines():
				my_songs.append(line)
		my_songs.sort()
	except FileNotFoundError:
		print('El archivo no existe')
	return my_songs


def write_text_to_file(file_path, list):
	with open(file_path, 'w') as file:
		for line in list:
			file.write(line)


def main():
	try:
		write_text_to_file("alpha_songs.txt", open_and_print_file_per_line('canciones.txt'))
	except Exception as ex:
		print(f'Error inesperdo: {ex}')
	exit()


main()