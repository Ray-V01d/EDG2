from tad.listas.nodos import NodoListasSimplementeEnlazada

if __name__ == "__main__":

    nodo1 = NodoListasSimplementeEnlazada(5)
    nodo2 = NodoListasSimplementeEnlazada(10)
    nodo3 = NodoListasSimplementeEnlazada(15)
    nodo4 = NodoListasSimplementeEnlazada(20)
    nodo5 = NodoListasSimplementeEnlazada(25)

nodo1.sig = nodo2
nodo1.sig.sig = nodo3
nodo1.sig.sig.sig = nodo4
nodo1.sig.sig.sig.sig = nodo5

# Creación de una lista Python de nodos (NO RECOMENDADO)

lista_py = [nodo1, nodo2, nodo3, nodo4, nodo5]
print(lista_py)
