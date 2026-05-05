from tad.arboles.nodos import NodoArbolBinario as NAB


class ArbolBinario:
    def __init__(self):
        self.__raiz = None

    def agregar(self, nueva_clave):
        self.raiz = self.__agregar(self.raiz, nueva_clave)

    def __agregar(self, sub_arbol, nueva_clave):
        if sub_arbol is None:
            sub_arbol = NAB(nueva_clave)