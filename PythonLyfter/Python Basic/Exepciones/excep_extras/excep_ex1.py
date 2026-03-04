

def name():
    try:
        user_name = str(input('Digite su nombre: '))
        if user_name.isdigit():
            raise ValueError
    except ValueError:
        print('\nEl nombre no puede ser un numero, intente nuevamente\n')
        name()
    age(user_name)


def age(user_name):
    try: 
        years_old = int(input('\nCual es su edad: \n'))
    except ValueError:
        print('\nNumero invalido, intente nuevamente\n')
        age(user_name)
    result(user_name, years_old)


def result(user, age):
    print(f'\nHola {user}, su edad es {age}.\n')
    exit()


def main():
    try:
        name()
    except Exception as ex:
        print(f'Error inesperado: {ex}')


main()