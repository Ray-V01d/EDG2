"""
pruebas simples para la clase ArbolBinario
"""

from tad.arboles.abin import ArbolBinario as ABin


def main():
    arbol = ABin()
    print("El árbol está vacío:", len(arbol))


    agr = [9, 6, 5, 10, 7, 8]
    print("Agregando", len(agr), "elementos al árbol:")
    for clave in agr:
        arbol.agregar(clave)
    print("Hecho. Buscando valores...")

    for clave in [5, 3, 7, 10, 1, 20]:
        resultado = arbol.buscar(clave)
        if resultado is None:
            print(f"Clave {clave}: no encontrada")
        else:
            print(f"Clave {clave}: encontrada")

    print(f"El árbol tiene {len(arbol)} nodos.")


if __name__ == '__main__':
    main()
