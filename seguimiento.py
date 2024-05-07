# hago una lista vacia para que cuando se llene la encuesta se agregue a esta
encuesta = []

# creo un bucle para los participantes
for i in range(100):
    # solicito los datos
    cedula = input("Ingrese la cédula del participante: ")
    genero = input("Ingrese el género del participante (masculino/femenino): ")
    ciudad = input(
        "Ingrese la ciudad de residencia del participante (Bogotá/Medellín/Cali): ")
    edad = input(
        "Ingrese el rango de edad del participante (joven/adulto/mayor): ")
    respuesta = input(
        "¿Está de acuerdo con el proceso de paz? (si/no/indiferente): ")

    # almacenar los datos
    participante = {"Cedula": cedula, "Genero": genero,
                    "Ciudad": ciudad, "Edad": edad, "Respuesta": respuesta}
    encuesta.append(participante)

# imprimir la lista
print(encuesta)
