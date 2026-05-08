from tad.listas.abin import ArbolBinario as ABin
from tad.arboles.nodos import NodoArbolBinario 


class ArbolBinarioBusqueda(ABin):
    def __init__(self):
        super().__init__()

    def agregar(self, nueva_clave):
        self.raiz = self.__agregar(self.raiz, nueva_clave)

    def __agregar(self, sub_arbol, nueva_clave):
        if sub_arbol is None:
            sub_arbol = NodoArbolBinario(nueva_clave)
        elif nueva_clave < sub_arbol.clave:
            sub_arbol.izq = self.__agregar(sub_arbol.izq, nueva_clave)
        elif nueva_clave > sub_arbol.clave:
            sub_arbol.der = self.__agregar(sub_arbol.der, nueva_clave)
        else:
            raise ValueError(f"La clave {nueva_clave} ya existe en el árbol.")
        return sub_arbol