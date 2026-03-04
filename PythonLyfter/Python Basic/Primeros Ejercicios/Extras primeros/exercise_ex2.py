print('~~~ SEGUNDOS ~~~')

sec = int(input('Digite sus segundos: '))
if sec < 600 : 
    print (f'Faltaron {600 - sec} segundos')
elif sec > 600 : 
    print ('Mayor')
else: 
    print('Igual')