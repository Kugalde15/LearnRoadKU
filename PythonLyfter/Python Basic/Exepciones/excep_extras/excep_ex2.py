

def capture():
    list_items = []
    for vals in range(5):
        values_list = input(f'Escriba el valor {vals+1}: ')
        list_items.append(values_list)
    convert(list_items)


def convert(list):
    print('\n>> Resultado: << \n')
    convert_values= []
    for item in list:
        try:
            if ''=='':
                item = int(item)
                convert_values.append(item)
                print(f'"{item}" convertido a entero')
            else:
                continue
        except ValueError:
            print(f'No se puede convertir "{item}" ')
            continue


def main():
    try:
        capture()
    except Exception as ex:
        print(f'Ocurrio un error inesperado: {ex}')
    exit()


main()