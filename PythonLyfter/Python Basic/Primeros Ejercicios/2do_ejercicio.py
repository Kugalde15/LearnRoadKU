print('---MAQUINA ALEATORIA---')
import random
numero_ram = random.randint(1, 10)
numero_persona = int(input('Digite un numero del 1 al 10: '))
while numero_persona != numero_ram: 
    print('No acertaste el numero, intenta nuevamente')
    numero_persona = int(input('Digite un numero del 1 al 10: '))
print('Felicidades, acertaste el numero!')