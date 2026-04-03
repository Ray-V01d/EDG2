"""
pruebas para la clase Pila

Copyright (C) 2026 Ray
SPDX-License-Identifier: GPL-3.0-or-later
"""


import os
from tad.listas.pila import Pila


def main():
    """Función principal
    """
    clear()
    sep()

    stk = Pila()

    test = {
        "es_vacía": True,
        "apilar": True,
        "desapilar": True,
        "cima": True,
        "len": True
    }

    if test["es_vacía"]:
        es_vacia(stk)

    if test["apilar"]:
        apilar(stk)

    if test["desapilar"]:
        desapilar(stk)

    if test["cima"]:
        cima(stk)

    if test["len"]:
        length(stk)


def clear():
    """Limpia la consola
    """
    os.system("cls" if os.name == "nt" else "clear")


def sep():
    """Agrega un separador constante
    """
    print()
    print("+" + "-" * 79 + "+")


def es_vacia(stk):
    """Prueba si la pila está vacía
    """
    print("=========TEST ES VACÍA=========")
    if stk.es_vacia():
        print("La pila se encuentra vacía")
    else:
        print("La pila NO se encuentra vacía")
    sep()


def apilar(stk):
    """Prueba a apilar datos a la pila
    """
    print("=========TEST APILAR=========")

    stack = "amolap acificap al oma"
    the = "|".join(stack[::-1]) + "|"

    print("Apilando los siguientes datos:", end=" ")
    for s in stack:
        stk.apilar(s)
        print(s, end="|")
    print()
    print(f"Pila (teórica): {the}")
    print()
    print("Pila actual:", stk)
    print("Cima actual:", stk.cima())
    print("Longitud actual:", len(stk))
    sep()


def desapilar(stk):
    """Prueba a desapilar datos de la pila
    """
    print("=========TEST DESAPILAR=========")

    des = 4

    print("Desapilando los siguientes datos:", end=" ")
    while des > 0:
        print(stk.cima(), end="|")
        stk.desapilar()
        des -= 1
    print()
    print(f"Pila desapilada: {stk}")
    print()
    while not stk.es_vacia():
        print(f"Desapilando dato: |{stk.cima()}|")
        stk.desapilar()
    print()
    print(f"Pila desapilada completamente: {stk}")
    sep()


def cima(stk):
    """Prueba a obtener la cima de la pila
    """
    print("=========TEST CIMA=========")
    print("La cima actual es:", stk.cima())
    sep()


def length(stk):
    """Prueba a obtener la cantidad de datos en la pila
    """
    print("=========TEST LEN=========")
    print("La pila tiene", len(stk), "elementos")
    sep()


if __name__ == "__main__":
    main()
