

def select_menu (fts_num):
    try:
        menu = int(input(
            'Que operacion desea realizar?:\n'
            '[1] Suma\n'
            '[2] Resta\n'
            '[3] Multiplicacion\n'
            '[4] Division\n'
            '[5] Borrar Resultado' \
            '\n==> '
            ))
        if menu <1 or menu >5:
            raise ValueError
        elif menu == 5:
            fts_num = 0
            print('\n>> Datos borrados <<\n')
            select_menu(fts_num)
        else:
            if fts_num == 0:
                fts_num = float(input('Cual es su primer numero?: \n==> '))
            calculator(menu, fts_num)
    except ValueError:
        print('\n>> Digite un valor valido <<\n')
        select_menu(fts_num)


def calculator(menu, fts_num):
    try:
        snd_number = float(input('Cual es se segundo numero?: \n==> '))
        if menu == 1:
            fts_num += snd_number
        elif menu == 2:
            fts_num -= snd_number
        elif menu == 3:
            fts_num *= snd_number
        elif menu == 4:
            fts_num /= snd_number
        print(f'\nEl resultado es: {round(fts_num, 2)}\n')
        print(f'Desea realizar otra operacion?: \n [1] Si\n [AnyNum] No')
        retun_menu = int(input('==> '))
        if retun_menu == 1:
            select_menu(fts_num)
        else:
            exit()
    except ValueError:
        print('\n>> Digite un valor valido <<\n')
        calculator(menu, fts_num)
    except ZeroDivisionError:
        print('\n>> Digite un valor valido, no puede dividir por "0" <<\n')
        calculator(menu, fts_num)


def main_program():
    try:
        fts_num = 0
        select_menu(fts_num)
    except Exception as ex:
        print(f'\n>> Hubo un error inesperado: {ex} <<\n')
        select_menu(fts_num)


main_program()