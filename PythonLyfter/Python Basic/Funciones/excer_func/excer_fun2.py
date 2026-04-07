

# def suma(num1, num2, num3):
#     result = num1+num2+num3
#     return result


# print(f'La suma es: {suma(12,23,48)}')

# even = []
# odd = []


# def even_or_odd():
#     others = (suma(9,2,6))
#     print(f'El numero es: {others}')
#     if others % 2 == 0:
#         even.append(others)
#         print(f'El numero {even} es par')
#     else:
#         odd.append(others)
#         print(f'El numero {odd} es impar')

# even_or_odd()

name = 'Keylor'

def full_name():
    global name
    last = 'Ugalde'
    name = name + ' ' + last


full_name()
print(name)