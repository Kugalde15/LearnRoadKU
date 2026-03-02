

samples = [12, 235, 543]

def sum(list1):
    result = 0
    for nums in list1:
        result = nums + result
    return result


result = sum(samples)
print(result)


# samples = []

# cant = int(input('Cuantos numeros deseas?: '))
# for num in range(cant):
#     nums = int(input('Escribe el numero ' + str(num+1) + ' : '))
#     samples.append(nums)
# print(samples)


# def sum(lista):
#     amount = 0
#     for num in lista:
#         amount += num
#     print(f'La suma es: {amount}')


# sum(samples)