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

def imprimir_palabra(palabra, letras_encontradas):
    for i in range(len(palabra)):
        if (palabra[i] in letras_encontradas) or palabra[i] == ' ':
            print(palabra[i], end=' ')
        else:
            print('_', end=' ')
    print('\n')

def validar_letra(letra, letras, letras_encontradas,letras_erroneas,vidas):
    if letra in letras:
        if letra not in letras_acertadas:
            letras_encontradas.append(letra)
        else:
            print('Esa letra ya la has ingresado')
    else:
        letras_erroneas.append(letra)
        vidas-=1
        print(vidas)

#####Variables

palabras = 'raqueta de tenis'.upper()
largo = len(re.sub(r"[^a-zA-Z0-9]","",palabras))
letras = set(re.sub(r"[^a-zA-Z0-9]","",palabras))
letras_acertadas = []
letras_erroneas = []
restantes = largo - len(letras_acertadas)
vidas = 5
#nombre = inicio()

while (vidas > 0 and (len(letras_acertadas) != len(letras))):
    imprimir_palabra(palabras,letras_acertadas)
    letra = input('Inserte letra: ').upper()
    validar_letra(letra,letras,letras_acertadas,letras_erroneas,vidas)
    print(vidas)
    