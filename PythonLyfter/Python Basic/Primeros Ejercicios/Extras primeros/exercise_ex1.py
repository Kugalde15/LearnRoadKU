print ('~~~ PRECIO DE PRODUCTOS') 

price = int(input('Digite el precio del producto: '))
if price < 100 : 
    discount2 = price * 0.02
    print('El precio final es de: ' , (price - discount2))
else: 
    discount10 = price * 0.10
    print('El precio final es de: ' , (price - discount10))