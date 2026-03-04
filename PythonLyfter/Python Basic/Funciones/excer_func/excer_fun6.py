my_consoles = 'Xbox-Nintendo-PlayStation-Atari-Sega-'

def sort_alph(str1):
    str_alph = []
    word = ''
    for char in str1:
        if char == '-':
            char = ''
            str_alph.append(word)
            word=""
        else: 
            word += char
    str_alph = sorted(str_alph)
    end = ""
    for index in range(len(str_alph)):
        end += str_alph[index]
        if (len(str_alph)-1) == index:
            break
        end += '-'
    return print(f'\nResultado: {end}\n')


sort_alph(my_consoles)