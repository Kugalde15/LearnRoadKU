def open_and_print_file_per_line(path, action, user_input):
	try:
		with open(path, action) as file:
			file.write(user_input)
	except FileNotFoundError:
		action = 'w'
		open_and_print_file_per_line('regsitro.txt')


def main():
	try:
		user_input = input('Escriba Texto: ')
		open_and_print_file_per_line('registro.txt', 'a', user_input)
	except Exception as ex:
		print(f'Error inesperdo: {ex}')
	exit()


main()