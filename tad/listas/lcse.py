from tad.listas.nodos import NodoListaSimplementeEnlazada as NLCSE


class ListaCircularSimplementeEnlazada:
    """Clase que implementa el funcionamiento de una lista circular simplemente
    enlazada. La lista es homogenea y validará el tipo de dato a añadir
    en la lista dependiendo del tipo de dato del primer nodo de la lista.

    """

    def __init__(self):
        """Método que inicializa una lista circular simplemente enlazada vacía

        """
        self.__cab = None
        self.__col = None

    def es_vacia(self):
        """Método que verifica si una lista está vacía

        Returns
        -------
        bool
            Retorna True si la lista está vacía, False en caso contrario.
        """
        return self.__cab is None

    def agregar(self, dat):
        """Método que agrega un nuevo nodo en la cola de la lista.


        Parameters
        ----------
        dat : object
            El nuevo dato a ser agregado a la lista

        Returns
        -------
        bool
            True si el nuevo dato es agregado. False en caso contrario
        """
        if not self.es_vacia() and type(dat) is not type(self.__cab.dato):
            return False
        new_nod = NLCSE(dat)
        if self.es_vacia():
            self.__cab = new_nod
            self.__col = new_nod
        else:
            self.__col.sig = new_nod
            self.__col = new_nod
        self.__col.sig = self.__cab
        return True

    def insertar(self, new, pos_rel=0):
        """Método que inserta un nuevo nodo en cualquier posición relativa de
        la lista. Si la lista está vacía, sólo podrá insertar en la posición
        [0]. De lo contrario cualquier posicións será válida.

        Parameters
        ----------
        new : object
            El nuevo dato a ser insertado en la lsita
        pos_rel : int, optional
            Posición relativa en la que se insertará el dato, by default 0

        Returns
        -------
        bool
            True si el nuevo dato es insertado. False en caso contrario
        """
        if type(pos_rel) is not int or pos_rel < 0:
            return False
        if not self.es_vacia() and type(new) is not type(self.__cab.dato):
            return False
        new_nod = NLCSE(new)
        if self.es_vacia():
            self.__cab = self.__col = new_nod
            new_nod.sig = new_nod
        else:
            n = len(self)
            pos_rel = pos_rel % n
            if pos_rel % n == 0:
                new_nod.sig = self.__cab
                self.__cab = new_nod
            else:
                nod_act = self.__cab
                pos_act = 0
                while pos_act < pos_rel - 1:
                    nod_act = nod_act.sig
                    pos_act += 1
                if nod_act == self.__col:
                    new_nod.sig = self.__cab
                    self.__cab = new_nod
                else:
                    new_nod.sig = nod_act.sig
                    nod_act.sig = new_nod
        self.__col.sig = self.__cab
        return True

    def suprimir(self, item, por_dato=True):
        """Método que suprime un nodo en la lista, puede ser por una
        posición o por un dato.

        Parameters
        ----------
        item : object|int
            Puede corresponder a la posición relativa donde se encuentra
            el nodo a suprimir o al dato del nodo a suprimir.
        por_dato : bool, optional
            Si es True, el método suprimirá la primera aparición del dato.
            Si es False, el método suprimirá el nodo en la posición relativa.
            , by default True

        Returns
        -------
        bool
            True si el nodo es suprimido. False en caso contrario
        """
        if type(por_dato) is not bool:
            return False
        if por_dato:
            return self.__suprimir_dato(item)
        else:
            if type(item) is not int or item < 0:
                return False
            return self.__suprimir_pos(item)

    def __suprimir_pos(self, pos_sup):
        if self.es_vacia() or pos_sup < 0:
            return False
        if self.__cab == self.__col:
            self.__cab = self.__col = None
            return True
        pos_sup = pos_sup % len(self)
        if pos_sup == 0:
            self.__cab = self.__cab.sig
            self.__col.sig = self.__cab
            return True
        nodo_actual = self.__cab
        pos_actual = 0
        while pos_actual < pos_sup - 1:
            nodo_actual = nodo_actual.sig
            pos_actual += 1
        if nodo_actual.sig == self.__cab:
            self.__cab = self.__cab.sig
            self.__col.sig = self.__cab
            return True
        if nodo_actual.sig == self.__col:
            self.__col = nodo_actual
        nodo_actual.sig = nodo_actual.sig.sig
        self.__col.sig = self.__cab
        return True

    def __suprimir_dato(self, dato_sup):
        if self.es_vacia():
            return False
        if self.__cab.dato == dato_sup:
            if self.__cab == self.__col:
                self.__cab = None
                self.__col = None
            else:
                self.__cab = self.__cab.sig
                self.__col.sig = self.__cab
            return True
        nodo_actual = self.__cab
        while (
            nodo_actual.sig != self.__cab
            and nodo_actual.sig.dato != dato_sup
        ):
            nodo_actual = nodo_actual.sig
        if nodo_actual.sig == self.__cab:
            return False
        if nodo_actual.sig == self.__col:
            self.__col = nodo_actual
        nodo_actual.sig = nodo_actual.sig.sig
        self.__col.sig = self.__cab
        return True

    def buscar(self, dato_buscar):
        """Método que busca el valor de un dato en la lista

        Parameters
        ----------
        dato_buscar : object|int
            Corresponde al valor del dato a ser buscado en la lista.

        Returns
        -------
        object
            Corresponde al dato encontrado en la lista.
            Retorna None si el dato no es encontrado.
        """
        if self.es_vacia():
            return None
        if dato_buscar == self.__cab.dato:
            return self.__cab
        if dato_buscar == self.__col.dato:
            return self.__col
        nodo_actual = self.__cab.sig
        while nodo_actual is not self.__col:
            if nodo_actual.dato == dato_buscar:
                return nodo_actual
            nodo_actual = nodo_actual.sig
        return None

    def buscar_cuantos(self, dato_buscar):
        """Método que cuenta el número de apariciones en la lista.

        Parameters
        ----------
        dato_buscar : object
            Corresponde al valor del dato a ser buscado.

        Returns
        -------
        int
            El número de apariciones del dato en la lista
        """
        if self.es_vacia():
            return 0
        nodo_actual = self.__cab
        contador = 0
        while True:
            if nodo_actual.dato == dato_buscar:
                contador += 1
            nodo_actual = nodo_actual.sig
            if nodo_actual == self.__cab:
                return contador

    def suerte(self, pos_rel):
        """Método que devuelve el dato en una posición relativa de la lista

        Parameters
        ----------
        pos_rel : int
            Corresponde a la posición del nodo a ser buscado en la lista.

        Returns
        -------
        object
            El dato encontrado en la lista.
        """
        if type(pos_rel) is not int or pos_rel < 0:
            return None
        if self.es_vacia():
            return None
        pos_rel = pos_rel % len(self)
        nodo_actual = self.__cab
        pos_actual = 0
        while pos_actual < pos_rel:
            nodo_actual = nodo_actual.sig
            pos_actual += 1
        return nodo_actual.dato

    def __str__(self):
        """Método que devuelve una cadena con los datos de la lista.
        Si la lsita está vacía devolverá una cadena sin datos.

        Returns
        -------
        str
            Si la lista no es vacía retornará una cadena en el formato
            (ejemplo para 4 datos):
            "⭕ --> |dato_0| --> |dato_1| --> |dato_2| --> ⭕" de lo contrario
            retornará una cadena con el siguiente formato:
            "⭕ --> ⭕"
        """
        if self.es_vacia():
            return "⭕ --> ⭕"
        resultado = "⭕ --> "
        nodo_actual = self.__cab
        while True:
            resultado += f"[{nodo_actual.dato}] --> "
            nodo_actual = nodo_actual.sig
            if nodo_actual == self.__cab:
                break
        resultado += "⭕"
        return resultado

    def __len__(self):
        """Método que calcula el tamaño de una lista

        Returns
        -------
        int
            Corresponde a la cantidad de nodos de la lista.
        """
        if self.es_vacia():
            return 0
        nodo_actual = self.__cab
        contador = 0
        while True:
            contador += 1
            nodo_actual = nodo_actual.sig
            if nodo_actual == self.__cab:
                return contador

    def __iter__(self):
        """Método que devuelve uno por uno los datos de cada nodo de la lista.

        Yields
        ------
        object
            El dato de cada nodo de la lista.
        """
        if self.es_vacia():
            return (())
        nodo_actual = self.__cab
        while True:
            yield nodo_actual.dato
            nodo_actual = nodo_actual.sig
            if nodo_actual == self.__cab:
                return
