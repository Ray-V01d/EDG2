"""
Módulo para implementar nodos para listas.

Autor: Ray
Año: 2026
Licencia: GNU GPL v3.0
"""


class Nodo:
    """Clase que corresponde a un nodo genérico para listas"""

    def __init__(self, dato):
        """Método constructor que incorpora un dato dentro de un nodo

        Parameters
        ----------
        dato : object
            El dato a ser almacenado en el nodo
        """
        self.dato = dato

    def __str__(self):
        return f"{self.dato}"

    def __repr__(self):
        return f"{self.dato}"


class NodoListaSimplementeEnlazada(Nodo):
    """Clase que corresponde a un nodo de una lista simplemente enlazada"""

    def __init__(self, dato) -> None:
        """Método constructor que incorpora un dato dentro de un nodo
        de lista simplemente enlazada

        Parameters
        ----------
        dato : object
            El dato a ser almacenado en el nodo
        """
        super().__init__(dato)
        self.sig: NodoListaSimplementeEnlazada | None = None


class NodoListaDoblementeEnlazada(Nodo):
    """Clase que corresponde a un nodo de una lista doblemente enlazada"""

    def __init__(self, dato) -> None:
        """Método constructor que incorpora un dato dentro de un nodo
        de lista doblemente enlazada

        Parameters
        ----------
        dato : object
            El dato a ser almacenado en el nodo
        """
        super().__init__(dato)
        self.sig: NodoListaDoblementeEnlazada | None = None
        self.ant: NodoListaDoblementeEnlazada | None = None
