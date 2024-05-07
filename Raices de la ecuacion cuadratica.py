# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:11:40 2023

@author: Sebastian_R
"""

print("Raices de la ecuacion cuadratica")

a=float(input("Digite el coeficiente cuadratico: \n"))
b=float(input("Digite el coeficiente lineal: \n"))
c=float(input("Digite el coeficiente independiente: \n"))

if a==0:
    print("Ecuacion no cuadratica")
else:
    D=b**2-4*a*c
    if D==0:
        
        x1=-b/(2*a)
        x2=x1
        print("Raices reales iguales", x1, x2)
    else:
        if D>0:
            x1=(-b+(D**(0.5))/(2*a))
            x2=(-b-(D**(0.5))/(2*a))
        
            print("Raices reales diferentes: ", x1, x2)
        
        else:
            x1=(-b+(D**0.5))/(2*a)
            x2=(-b-(D**0.5))/(2*a)
            print("Raices complejas", x1, x2)
            
        
        