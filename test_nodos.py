"""
Módulo de pruebas para la clase Nodo.

Autor: Ray
Año: 2026
Licencia: GNU GPL v2.0
"""


from tad.listas.nodos import NodoListaSimplementeEnlazada

if __name__ == "__main__":

    nodo1 = NodoListaSimplementeEnlazada(5)
    nodo2 = NodoListaSimplementeEnlazada(10)
    nodo3 = NodoListaSimplementeEnlazada(15)
    nodo4 = NodoListaSimplementeEnlazada(20)
    nodo5 = NodoListaSimplementeEnlazada(25)

nodo1.sig = nodo2
nodo1.sig.sig = nodo3
nodo1.sig.sig.sig = nodo4
nodo1.sig.sig.sig.sig = nodo5

# Creación de una lista Python de nodos (NO RECOMENDADO)

lista_py = [nodo1, nodo2, nodo3, nodo4, nodo5]
print(lista_py)
