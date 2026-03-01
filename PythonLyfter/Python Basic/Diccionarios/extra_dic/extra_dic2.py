# Agrupar empleados por departamento
# Dada una lista de empleados donde cada uno tiene nombre, correo y departamento, cree un diccionario
# que agrupe los empleados por su departamento:

employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

ti = []
sales = []
rh= []

for dep in employees:   
    if dep['department'] == 'Ventas':
        sales.append(dep)
    elif dep["department"] == 'TI':
        ti.append(dep)
    else:
        rh.append(dep)

# print(f'\n{ti}')
# print(f'\n{sales}')
# print(f'\n{rh}')

departments = {
'ventas':sales, 
'RRHH':rh,
'TI':ti
}
print(f'\n\n{departments["RRHH"]} \n\n{departments["TI"]} \n\n{departments["ventas"]}\n')