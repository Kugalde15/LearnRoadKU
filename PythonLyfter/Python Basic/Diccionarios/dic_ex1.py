# Cree un diccionario que guarde la siguiente información sobre un hotel:

hotel = {
'Hotel Name' : 'Hotel Boyeros',
'stars' : '3 stars', 
'rooms': 
[{'room number' : 24, 
'floor' : 2 ,
'price': 20000}]
}

print (f'\n{hotel["rooms"][0]['floor']}\n')

for roomi, val in hotel.items():
    print(f'\n{roomi} --> {val}\n')