# Cree una función que reciba una lista de palabras y un número n, y retorne una nueva lista con solo las 
# palabras que tengan más de n letras.

user_list = []

user_result = []

def qty_letters(list_u, rlt_list):
    for words in (range(5)):
        words = input(f'Cual es su {words + 1}º palabra: ')
        list_u.append(words)
    qty_words = int(input('Cuantas letras debe tener?: '))
    for user_words in list_u:
        if len(user_words) >= qty_words:
            rlt_list.append(user_words)
    print(f'\nLista del usuario: {user_list}\n')
    print(f'Resultado: {user_result}\n')


qty_letters(user_list, user_result)