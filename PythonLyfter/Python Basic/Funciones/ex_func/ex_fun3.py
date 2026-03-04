# Cree una función que reciba un string y retorne cuántas vocales contiene

def vocals_counter():
    user_word = input('\nEscriba el texto que desea revisar: ')
    counter = 0
    for vocals in user_word.lower():
        if vocals == 'a' or vocals == 'e' or vocals == 'i' or vocals == 'o' or vocals == 'u':
            counter += 1
    print(f'\nEl texto contiene "{counter}" vocales\n')


vocals_counter()