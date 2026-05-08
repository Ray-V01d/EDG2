from tad.arboles.abin import ArbolBinario as ABin
from tad.arboles.nodos import NodoArbolBinario as NAB
from tad.arboles.excepciones import DuplicatedKeyError


class ArbolBinarioBusqueda(ABin):
    def __init__(self):
        super().__init__()

    def agregar(self, nueva_clave):
        self.raiz = self.__agregar(self.raiz, nueva_clave)

    def __agregar(self, sub_arbol, nueva_clave):
        if sub_arbol is None:
            sub_arbol = NAB(nueva_clave)
        elif nueva_clave < sub_arbol.clave:
            sub_arbol.izq = self.__agregar(sub_arbol.izq, nueva_clave)
        elif nueva_clave > sub_arbol.clave:
            sub_arbol.der = self.__agregar(sub_arbol.der, nueva_clave)
        else:
            raise DuplicatedKeyError(f"{nueva_clave}")
        return sub_arbol