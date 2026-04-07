numbers = []

for q in range(10):
    n = int(input("Ingresa un número: "))
    numbers.append(n)

num_max = numbers[0]

for number in numbers:
    if number > num_max:
        num_max = number

print(f'Los numeros son', numbers, 'y el numero mas alto es: ', num_max)