from tad.arboles.nodos import NodoArbolBinario as NAB
from random import choice, randint


class ArbolBinario:
    def __init__(self):
        self.__raiz = None

    def agregar(self, nueva_clave):
        self.__raiz = self.__agregar(self.__raiz, nueva_clave)

    def __agregar(self, sub_arbol, nueva_clave):
        if sub_arbol is None:
            return NAB(nueva_clave)

        if randint(0, 1) == 0:
            sub_arbol.izq = self.__agregar(sub_arbol.izq, nueva_clave)
        else:
            sub_arbol.der = self.__agregar(sub_arbol.der, nueva_clave)
        return sub_arbol
    
    def buscar(self, clave_buscar):
        return self.__buscar(self.__raiz, clave_buscar)

    def __buscar(self, sub_arbol, clave_buscar):
        if sub_arbol is None:
            return None
        elif sub_arbol.clave == clave_buscar:
            return sub_arbol.clave
        izq = self.__buscar(sub_arbol.izq, clave_buscar)

        if izq is not None:
            return izq
        der = self.__buscar(sub_arbol.der, clave_buscar)

        if der is not None:
            return der
        return None