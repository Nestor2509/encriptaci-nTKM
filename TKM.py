import array
from multiprocessing.dummy import Array
from random import random
from string import ascii_letters
from array import array
import random
from typing import Text
from xml.etree.ElementTree import tostring

def llenarmatriz(Mn,jn,bn,an,Texto):
    p=len(Texto)
    for bn in range (jn):
        print('[' +str(an)+']['+str(bn)+']')
        Mn[bn]=random.randint(1,27)

def to_ascii(text):
    ascii_values = [ord(character) for character in text]
    return ascii_values

def codificación(TextoC,M):
    p=len(TextoC)
    bn=0
    for bn in range (p):
        Texto[bn]= M[bn]*TextoC[bn] 
     
A= list(map(chr,range(97,123)))
#contadores
a=0 
b=0
m=0
n=0
M=[n]*m 
j=m 

#Codificación de texto
print("Codifica TKM / guarda tu llave")
#for a in range (i):
print('Ingresa el texto a codificar')
Texto=str(input())
Texto=to_ascii(Texto)
print(Texto)
m=len(Texto)
n=len(Texto)
M=[n]*m
j=m
llenarmatriz(M,j,b,a,Texto)
print("Tu llave es")
print (M)

codificación(Texto,M)
print("Tu Cifrado es:",Texto)

