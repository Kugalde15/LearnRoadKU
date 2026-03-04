def open_and_print_file_per_line(path):
	my_string = ''
	try:
		with open(path) as file:
			for line in file.readlines():
				my_string += line.rstrip('\n') + ' '
	except FileNotFoundError:
		print('El archivo no existe')
	return my_string


def write_text_to_file(file_path, txt):
	with open(file_path, 'w') as file:
		for line in txt:
			file.write(line)


def main():
	try:
		write_text_to_file("line_greetings.txt", open_and_print_file_per_line('greetings.txt'))
	except Exception as ex:
		print(f'Error inesperdo: {ex}')
	exit()


main()