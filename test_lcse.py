"""
pruebas para la clase ListaCircularSimplementeEnlazada

Copyright (C) 2026 Ray
SPDX-License-Identifier: GPL-3.0-or-later
"""


import os
from tad.listas.lcse import ListaCircularSimplementeEnlazada as LCSE


def main():
    """Función principal
    """
    clear()
    lst = LCSE()

    test = {
        "agregar": True,
        "insertar": True,
        "suprimir_pos": True,
        "suprimir_dato": True,
        "buscar": True,
        "buscar_cuantos": True,
        "suerte": True,
        "metodos_magicos": True,
    }

    if test["agregar"]:
        agregar(lst)

    if test["insertar"]:
        insertar(lst)

    if test["suprimir_pos"]:
        suprimir_pos(lst)

    if test["suprimir_dato"]:
        suprimir_dato(lst)

    if test["buscar"]:
        buscar(lst)

    if test["buscar_cuantos"]:
        buscar_cuantos(lst)

    if test["suerte"]:
        suerte(lst)

    if test["metodos_magicos"]:
        metodos_magicos(lst)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def separador():
    print("+" + "=" * 79 + "+")


def agregar(lst):
    separador()
    print("=== PRUEBA AGREGAR ===")

    add = [1, 3, 5, 7]

    for a in add:
        lst.agregar(a)
        print(lst)
        print()


def insertar(lst):
    separador()
    print("=== PRUEBA INSERTAR ===")

    valores = [0, 2, 4, 6]
    posiciones = [20, 14, 19, 11]

    for v, p in zip(valores, posiciones):
        lst.insertar(v, p)
        print(lst)
        print()


def suprimir_pos(lst):
    separador()
    print("=== PRUEBA SUPRIMIR POR POSICIÓN ===")

    pruebas = [16, 20, 27, -5, 18, 26, 22, 32, 3, 4]

    for p in pruebas:
        lst.suprimir(p, False)
        print(lst)
        print()


def suprimir_dato(lst):
    separador()
    print("=== PRUEBA SUPRIMIR POR DATO ===")

    pruebas = ["Nada", 100, 0, 7, 3, 1, 6, 5, 2]

    for p in pruebas:
        lst.suprimir(p, True)
        print(lst)
        print()

    lst.agregar(7)
    print(lst)
    print()

    suprimir = [4, 7, 3]
    for s in suprimir:
        lst.suprimir(s, True)
        print(lst)
        print()


def buscar(lst):
    separador()
    print("=== PRUEBA BUSCAR ===")

    search = [0, 7, 4, 1000]
    for b in search:
        print(f"Buscar {b}:", lst.buscar(b))
    print()


def buscar_cuantos(lst):
    separador()
    print("=== PRUEBA BUSCAR CUANTOS ===")

    many = [4, 2]
    for b in many:
        print(f"Buscar cuántos {b}:", lst.buscar_cuantos(b))
    print()


def suerte(lst):
    separador()
    print("=== PRUEBA SUERTE ===")

    for x in [17, 52, 28, 37, 9]:
        print(f"Suerte {x}:", lst.suerte(x))
    print()


def metodos_magicos(lst):
    separador()
    print("=== PRUEBA MÉTODOS MÁGICOS ===")

    print(f'La lista tiene {len(lst)} nodos')
    print("Iteración:")
    for i in lst:
        print(f'[{i}]', end=' ')
    print()


if __name__ == "__main__":
    main()
