"""
Módulo para implementar una lista simplemente enlazada.

Autor: Ray
Año: 2026
Licencia: GNU GPL v2.0
"""
from tad.listas.nodos import NodoListaSimplementeEnlazada as NLSE


class ListaSimplementeEnlazada:
    """Implementaciónn de una lista simplemente enlazada.
    """

    def __init__(self):
        """Método que inicializa una lista simplemente enlazada vacía.
        """
        self.__cab = None

    def __len__(self):
        length = 0
        nodo_actual = self.__cab

        while nodo_actual:
            nodo_actual = nodo_actual.sig
            length += 1
        return length

    def __str__(self):
        """Devuelve una representación en cadena de la lista.
        Si está vacía, devuelve '📜'.
        """
        salida = "📜"
        nodo_actual = self.__cab

        while nodo_actual:
            salida += f" |{nodo_actual.dato}|"
            if nodo_actual.sig:
                salida += " ->"
            nodo_actual = nodo_actual.sig
        return salida

    def __iter__(self):
        """Método que permite iterar sobre los datos de la lista
        para que sean tratados por fuera de la misma
        """
        nodo_actual = self.__cab

        while nodo_actual:
            yield nodo_actual.dato
            nodo_actual = nodo_actual.sig

    def es_vacia(self):
        """Método que verifica si una lista está vacia o no.

        Returns
        -------
        bool
            Devuelve True si la lista es vacía, False en caso contrario.
        """
        return self.__cab is None

    def agregar(self, nuevo_dato):
        """Método que agrega un nuevo nodo al final de la lista.
        La lista es homogénea: solo se permiten elementos del mismo
        tipo que el primer nodo insertado.

        Parameters
        ----------
        nuevo_dato : object
            Dato a agregar en la lista.

        Returns
        -------
        bool
            True cuando el nuevo dato es agregado correctamente.
            False en caso contrario.
        """
        nuevo_nodo = NLSE(nuevo_dato)
        if self.es_vacia():
            self.__cab = nuevo_nodo

        elif type(nuevo_dato) is type(self.__cab.dato):
            nodo_actual = self.__cab
            while nodo_actual.sig is not None:
                nodo_actual = nodo_actual.sig
            nodo_actual.sig = nuevo_nodo
        else:
            return False
        return True

    def explorar(self):
        """Imprime los datos de la lista si no está vacía.
        """
        salida = "📕"
        if self.es_vacia():
            print(f"{salida}" + " Lista vacía")
            return
        nodo_actual = self.__cab

        while nodo_actual:
            salida += f" |{nodo_actual.dato}|"
            if nodo_actual.sig:
                salida += " ->"
            nodo_actual = nodo_actual.sig
        print(salida)

    def buscar(self, item, por_dato=True):
        """Método de búsqueda en una lista

        Parameters
        ----------
        item : object | int
            Puede corresponder al valor del dato a ser buscado en la lista o a
            la posición en la lista a obtener el dato.
        por_dato : bool, optional
            Si es True, el método buscará por valor.
            Si es False, buscará por índice.
            Por defecto True.

        Returns
        -------
        object|None
            Devuelve el dato encontrado o None si no se encuentra.
        """
        if por_dato:
            return self.__buscar_dato(item)
        else:
            if not isinstance(item, int) or item < 0:
                raise IndexError("item debe ser un entero no negativo")
            return self.__buscar_indice(item)

    def __buscar_dato(self, dato_buscar):
        nodo_actual = self.__cab

        while nodo_actual:
            if nodo_actual.dato == dato_buscar:
                return nodo_actual.dato
            nodo_actual = nodo_actual.sig
        return None

    def __buscar_indice(self, pos_buscar):
        nodo_actual = self.__cab
        pos_actual = 0

        while nodo_actual and pos_actual < pos_buscar:
            pos_actual += 1
            nodo_actual = nodo_actual.sig
        return nodo_actual.dato if nodo_actual else None

    def insertar(self, nuevo_dato, pos_ins=0):
        """Inserta un nuevo nodo en una posición específica.
        Si la posición es 0, se inserta al inicio.

        Parameters
        ----------
        nuevo_dato : object
            El nuevo dato a ser insertado en la lista.
        pos_ins : int, optional
            Posición a insertar en la lista.

        Returns
        -------
        bool
            True cuando el dato es insertado en la lista.
            False en caso contrario
        """
        if not isinstance(pos_ins, int) or pos_ins < 0:
            return False

        if not self.es_vacia() and (
            type(nuevo_dato) is not type(self.__cab.dato)
        ):
            return False
        nuevo_nodo = NLSE(nuevo_dato)

        if pos_ins == 0:
            nuevo_nodo.sig = self.__cab
            self.__cab = nuevo_nodo
            return True
        nodo_actual = self.__cab
        pos_actual = 0

        while pos_actual < pos_ins - 1 and nodo_actual is not None:
            nodo_actual = nodo_actual.sig
            pos_actual += 1

        if nodo_actual is None:
            return False
        nuevo_nodo.sig = nodo_actual.sig
        nodo_actual.sig = nuevo_nodo
        return True

    def suprimir(self, item, por_dato=True):
        """Elimina nodos de la lista por valor o por posición.

        Parameters
        ----------
        item : object | int
            Valor o posición del nodo a eliminar.
        por_dato : bool, optional
            Si True, elimina por valor.
            Si False, elimina por índice.

        Returns
        -------
        bool
            True si se eliminó correctamente, False en caso contrario.
        """
        if not por_dato:
            if not isinstance(item, int) or item < 0 or item >= len(self):
                return False
            return self.__suprimir_pos(item)
        else:
            return self.__suprimir_dato(item)

    def __suprimir_pos(self, pos_sup):
        if self.es_vacia() or pos_sup < 0:
            return False

        if pos_sup == 0:
            self.__cab = self.__cab.sig
            return True
        nodo_actual = self.__cab
        pos_actual = 0

        while pos_actual < pos_sup - 1 and nodo_actual.sig:
            nodo_actual = nodo_actual.sig
            pos_actual += 1

        if nodo_actual.sig:
            nodo_actual.sig = nodo_actual.sig.sig
            return True
        return False

    def __suprimir_dato(self, dato_sup):
        if self.es_vacia():
            return False

        if self.__cab and self.__cab.dato == dato_sup:
            self.__cab = self.__cab.sig
            return True
        nodo_actual = self.__cab

        while nodo_actual and nodo_actual.sig:
            if nodo_actual.sig.dato == dato_sup:
                nodo_actual.sig = nodo_actual.sig.sig
                return True  # 🔥 detenerse aquí
            nodo_actual = nodo_actual.sig
        return False

    def __getitem__(self, index):
        """Permite acceder a los elementos de la lista mediante índices.

        Parameters
        ----------
        index : int
            Posición del elemento a obtener.

        Returns
        -------
        object
            Dato almacenado en la posición indicada.

        Raises
        ------
        TypeError
            Si el índice no es un entero.
        IndexError
            Si el índice es negativo o está fuera de rango.
        """
        if not isinstance(index, int):
            raise TypeError("El índice debe ser un entero")

        if index < 0:
            raise IndexError("Índice fuera de rango")
        nodo_actual = self.__cab
        pos_actual = 0

        while nodo_actual and pos_actual < index:
            nodo_actual = nodo_actual.sig
            pos_actual += 1

        if nodo_actual:
            return nodo_actual.dato
        raise IndexError("Índice fuera de rango")
