

def def_elements():
    elements_list = []
    for ele in range(5):
        element = input(f'\nDigite el elemento # {ele+1}: ')
        elements_list.append(element)
    convert_float(elements_list)


def convert_float(list):
    print()
    sum_floats = []
    for ele in list:
        try:
            if '' == '':
                ele = float(ele)
                sum_floats.append(ele)
                print(f'" {ele} " sumado correctamente')
            else:
                ValueError
        except ValueError:
            print(f'Elemento invalido: {ele}')
            continue
    print(f'\nEl resultado es: {sum(sum_floats)}')


def main():
    try:
        def_elements()
    except Exception as ex:
        print(f'\nError inesperado: {ex}')


main()