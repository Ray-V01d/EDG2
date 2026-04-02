"""
Módulo para implementar nodos para listas.

Autor: Ray
Año: 2026
Licencia: GNU GPL v2.0
"""


class NodoListaSimplementeEnlazada:
    """Clase que corresponde a un nodo de una lista simplemente enlazada"""

    def __init__(self, dato):
        """Método contructo que incorpora un dato dentro de un nodo
           de lista simplemente enlazada.

        Parameters
        ----------
        dato : object
            Corresponde al valor que se va a guardar al interior del nodo
        """
        self.dato = dato
        self.sig = None

    def __str__(self):
        return f"{self.dato}"

    def __repr__(self):
        return f"{self.dato}"


class NodoListaDoblementeEnlazada(NodoListaSimplementeEnlazada):
    """Clase que corresponde a un nodo de una lista simplemente enlazada"""

    def __init__(self, dato):
        """Método contructo que incorpora un dato dentro de un nodo
           de lista doblemente enlazada.

        Parameters
        ----------
        dato : object
            Corresponde al valor que se va a guardar al interior del nodo
        """

        self.ant = None
