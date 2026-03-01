print('~~~ NOTAS ~~~')
notas_apro = 0
notas_desa = 0
promedio_total = 0
promedio_apro = 0
promedio_desa = 0
contador = 1
total_notas = int(input('Cuantas notas tienes?: '))
notas = 0
while contador <= total_notas : 
    notas = int(input('Cual es su nota: '))
    if notas >= 70 :
        notas_apro += 1
        promedio_apro = promedio_apro + notas 
        promedio_total = promedio_total + notas
        contador += 1
    else : 
        notas_desa += 1
        promedio_desa += notas
        promedio_total += notas
        contador += 1
pro_a = promedio_apro / notas_apro
pro_d = promedio_desa / notas_desa
pro_t = (promedio_apro + promedio_desa) / total_notas

print (f'''El resultado de sus notas aprobadas es:
    Notas aprobadas: {notas_apro} 
    Promedio de notas aprobadas: {pro_a}'''
    )
print (f'''El resultado de sus notas desaprobadas es: 
    Notas desaprobadas: {notas_desa} 
    Promedio de notas desaprobadas: {pro_d}'''
    )
print ('El promedio total es de: ' , pro_t)