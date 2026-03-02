

def find_prime():
    list_prime = []
    ram_nums = [2,12,41,56,89,13,75,15,123,159,119]
    for nums in ram_nums:
        div = [2,3,4,5,6,7,8,9]
        counter = 0
        for divis in div:
            if nums == 2:
                list_prime.append(nums)
                break
            if nums==divis and nums==2:
                divis +=1 
            elif not nums % divis == 0:
                counter+=1
            if counter == 8:
                list_prime.append(nums)
    print(f'\nLos numeros primos son: {list_prime}\n')
    return list_prime


find_prime()