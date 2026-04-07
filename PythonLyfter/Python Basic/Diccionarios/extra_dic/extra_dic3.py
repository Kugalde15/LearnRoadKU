# Dada una lista de productos vendidos, donde cada uno tiene categoría y precio, cree un diccionario 
# que acumule el total por categoría.

products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

elec = 0
furni = 0

for val in products:
    if val['category'] == 'Electrónica':
        elec = val['price'] + elec
    else:
        furni=val['price'] + furni

tl_by_pro = [
{'Electrónica': elec},
{'Muebles' : furni},
]

print(f'\n {tl_by_pro}\n')