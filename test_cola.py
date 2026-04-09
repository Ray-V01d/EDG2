"""
pruebas para la clase Pila

Copyright (C) 2026 Ray
SPDX-License-Identifier: GPL-3.0-or-later
"""


import os
from tad.listas.cola import Cola


def main():
    """Función principal
    """
    clear()
    sep()

    que = Cola()

    test = {
        "encolar": True,
        "desencolar": True
    }

    if test["encolar"]:
        print("Cola vacía:", que)
        es_vacia(que)
        encolar(que)
        frente(que)
        length(que)

    if test["desencolar"]:
        es_vacia(que)
        desencolar(que)
        frente(que)
        length(que)


def clear():
    """Limpia la consola
    """
    os.system("cls" if os.name == "nt" else "clear")


def sep():
    """Agrega un separador constante
    """
    print()
    print("+" + "-" * 79 + "+")


def es_vacia(que):
    """Prueba si la pila está vacía
    """
    print("=========TEST ES VACÍA=========")
    if que.es_vacia():
        print("La cola se encuentra vacía:", que)
    else:
        print("La cola NO se encuentra vacía:", que)
    sep()


def encolar(que):
    """Prueba el método encolar
    """
    print("=========TEST ENCOLAR=========")

    datos = "3.14159265358979"
    the = "|".join(datos) + "|"

    print("Encolando datos:", end=" ")

    for d in datos:
        print(f"{d}", end="|")
        que.encolar(d)
    print()
    print(f"Cola (teóricamente): {the}")
    print()
    print("Cola actual:", que)
    sep()


def desencolar(que):
    """Prueba el método desencolar
    """
    print("=========TEST DESENCOLAR=========")

    des = 4

    print("Desencolando los siguientes datos:", end=" ")
    while des > 0 and not que.es_vacia():
        dat = que.desencolar()
        print(f"{dat}", end="|")
        des -= 1
    print()
    print("Cola desencolada:", que)
    print()
    sep()


def frente(que):
    """Prueba a obtener el frente de la cola
    """
    print("=========TEST FRENTE=========")
    if not que.es_vacia():
        print("Frente actual:", que.frente())
    else:
        print("La cola está vacía, no hay frente.")
    sep()


def length(que):
    """Prueba el tamaño de la cola 🍑
    """
    print("=========TEST LENGTH=========")
    print("Tamaño actual:", len(que))
    sep()


if __name__ == "__main__":
    main()
