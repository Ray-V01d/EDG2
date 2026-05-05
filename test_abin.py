"""
pruebas simples para la clase ArbolBinario
"""

from tad.arboles.abin import ArbolBinario as ABin


def main():
    arbol = ABin()

    print("Agregar elementos al árbol:")
    arbol.agregar(5)
    arbol.agregar(3)
    arbol.agregar(7)
    arbol.agregar(10)
    arbol.agregar(1)
    print("Hecho. Buscando valores...")

    for clave in [5, 3, 7, 10, 1, 20]:
        resultado = arbol.buscar(clave)
        if resultado is None:
            print(f"Clave {clave}: no encontrada")
        else:
            print(f"Clave {clave}: encontrada")


if __name__ == '__main__':
    main()
