import sys
import os
import random
import time
import re




def inicio():
    print("\nBienvenido al juego del ahorcado\n")
    nombre = input("\tIngresa tu nombre: ")
    print("\tHola " + nombre + "! Suerte, Exitos!")
    time.sleep(2)
    print("\tEl Juego esta por empezar\nEmpieza el ahorcado")
    time.sleep(3)
    return nombre



#####Variables

palabras = 'raqueta de tenis'.upper()
largo = len(re.sub(r"[^a-zA-Z0-9]","",palabras))
letras = set(re.sub(r"[^a-zA-Z0-9]","",palabras))
letras_acertadas = []
letras_erroneas = []
restantes = largo - len(letras_acertadas)
nombre = inicio()

while True:
    letra = input('Inserte letra: ').upper()
    for i in range(len(palabras)):
		


