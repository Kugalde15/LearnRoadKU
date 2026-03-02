# Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto.

word = input('Escriba su palabra: ')

char = input('Ingrese el caracter que desea buscar: ')


def search_word(word1, char1):
    counter = 0
    for letters in word1:
        if letters.lower() == char1.lower():
            counter += 1
    return counter


print(f'\nLa Letra "{char}" aparece {search_word(word,char)} veces. \n')