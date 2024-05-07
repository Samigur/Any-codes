# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Club de pesca")
n=int(input("Ingrese número de participantes: \n"))
lm=0
pm=0
tm=0
th=0
pa=pb=pc=pd=slong=0

for i in range(n):
    nombre=input("Digite el nombre del participante: \n")
    longitud=float(input("Ingrese la longitud de la trucha (cms):  \n"))
    peso_trucha=float(input("Ingrese el peso de la trucha (grs): \n"))
    genero=input("Ingrese el genero del participante: F (Femenino). M (Masculino): \n")
    edad=int(input("Digite edad del participante"))
    
    #aqui contamos el ganador
    
    if longitud>lm and peso_trucha>pm:
        nombreg=nombre
        lm=longitud
        pm=peso_trucha
        
    if genero== "F":
        tm+=1
    else:
       if genero== "M":
            th+=1
            
    if edad>0 and edad<=19:
        cat="A"
    if edad>20 and edad<=29:
        cat="B"
    if edad>30 and edad<=39:
        cat="C"
    if edad>=40:
        cat="D"
        #aqui encontramos peso por categoria
    if cat=="A":
        pa+=peso_trucha
    if cat=="B":
        pb+=peso_trucha
    if cat=="C":
        pc+=peso_trucha
    if cat=="D":
        pd+=peso_trucha
        #aqui sumamos longitudes
        slong+=longitud
        
    print(f"El ganador fue:  {nombreg})
#aqui determinamos si ganaron los hombre o las mujeres
if th>tm:
    print("Ganaron los hombres!!!")
else:
    if tm>th
    print("Ganaron las mujeres!!!")
else:
    print("Hubo un empate entre hombres y mujeres!!!")
    
#peso total por categoria

    print(f"El peso por categoria ´A´ es: {pa}")
    print(f"El peso por categoria ´B´ es: {pb}")
    print(f"El peso por categoria ´C´ es: {pc}")
    print(f"El peso por categoria ´D´ es: {pd}")
#longitud promedio de truchas atrapadas
    print("Longitud promedio de truchas es: ",slong/n,"cms")



      
        
        
        
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    