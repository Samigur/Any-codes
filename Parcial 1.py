num_estructuras = int(input("Ingrese el número de estructuras armadas: "))

mayor_integrantes = 0
mayor_hombres = 0
mayor_mujeres = 0
total_hombres = 0
total_mujeres = 0
total_menores = 0
menor_armas = float('inf')
estructura_menor_armas = ""

for i in range(num_estructuras):
    print(f"Ingrese información para la estructura {i+1}:")

    nombre_estructura = input("Nombre del grupo o de la organización armada: ")
    num_integrantes = int(input("Número de integrantes totales: "))
    num_hombres = int(input("Cantidad de hombres: "))
    num_mujeres = int(input("Cantidad de mujeres: "))
    num_menores = int(input("Cantidad de menores de edad en sus filas: "))
    num_armas = int(input("Número de armas que se entregarán por parte de la estructura: "))

    if num_integrantes > mayor_integrantes:
        mayor_integrantes = num_integrantes
        estructura_mayor_integrantes = nombre_estructura
    
    if num_hombres > mayor_hombres:
        mayor_hombres = num_hombres
        total_hombres += num_hombres
        total_mujeres += num_mujeres
        
    elif num_mujeres > mayor_mujeres:
        mayor_mujeres = num_mujeres
        total_mujeres += num_mujeres
        total_hombres += num_hombres
        
    else:
        total_hombres += num_hombres
        total_mujeres += num_mujeres
    
    total_menores += num_menores
    
    if num_armas < menor_armas:
        menor_armas = num_armas
        estructura_menor_armas = nombre_estructura

porcentaje_mayor_genero = max(mayor_hombres, mayor_mujeres) / sum([total_hombres, total_mujeres]) * 100

print(f"La estructura armada con el mayor número de integrantes es: {estructura_mayor_integrantes}")
print(f"El género con mayor población en las estructuras armadas es: {'Hombres' if mayor_hombres > mayor_mujeres else 'Mujeres'}")
print(f"El porcentaje de la cantidad mayor de género respecto al total de integrantes ilegalmente armados es: {porcentaje_mayor_genero:.2f}%")
print(f"El número total de menores que hacen parte de las filas es: {total_menores}")
print(f"La estructura que entregará el menor número de armas es: {estructura_menor_armas}")
