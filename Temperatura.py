# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 12:13:56 2023

@author: Sebas_Ramirezzz
"""


import random

print("Creacion de temperatura: ")
def Crearvector():
    
    V=[0]*7
    
    for i in range(7):
        
        
        V[i]=random.random()*40
    return V
def Mint(T):
    tmin=40
    for i in range(7):
        if T[i]<tmin:
            tmin=T[i]
            diamin=i
    return tmin, diamin
        

T=Crearvector()
print(T)
tmin,diamin=Mint(T)
print(f"La menor temperatura fue {tmin} y fue el dia {diamin}")
      


