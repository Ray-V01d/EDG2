"""
cola.py - Implementación de una cola de datos

Copyright (C) 2026 Ray
SPDX-License-Identifier: GPL-3.0-or-later
"""


from tad.listas.nodos import NodoListaSimplementeEnlazada as NLSE


class Cola:
    """Clase que implementa el funcionamiento del TAD Cola
    """
    def __init__(self):
        """Método que realiza la creación e inicialización de la Cola
        """
        self.__fre = None
        self.__ter = None

    def es_vacia(self):
        """Método que verifica si la cola se encuentra vacía

        Returns
        -------
        bool
            Retorna True si la cola es vacia. False en caso contrario
        """
        return self.__fre is None

    def __homogeneo(self, dato):
        if self.es_vacia():
            return True
        return type(dato) is type(self.__fre.dato)

    def encolar(self, nuevo_dato):
        """Método que adiciona un nuevo dato al final de la cola. Realizar la
        validación de Homogeneidad para cada dato ingresado a la cola

        Parameters
        ----------
        nuevo_dato : object
            El nuevo dato a ser adicionado a la cola

        Returns
        -------
        bool
            True si nuevo_dato fue encolado. False en caso contrario
        """
        if self.es_vacia():
            self.__fre = NLSE(nuevo_dato)
            self.__ter = self.__fre
            return True
        if self.__homogeneo(nuevo_dato):
            self.__ter.siguiente = NLSE(nuevo_dato)
            self.__ter = self.__ter.siguiente
            return True
        return False

    def desencolar(self):
        """Método que saca/quita el primer nodo (elimina el nodo) de la cola
        y retorna su dato

        Returns
        -------
        object | None
            El dato del primer nodo de la cola y None cuando la cola no
            contenga nodos/datos
        """
        if not self.es_vacia():
            dato = self.__fre.dato
            self.__fre = self.__fre.siguiente
            return dato
        return None

    def frente(self):
        """Método que retorna el dato del primer nodo de la cola, sin quitarlo
        de la misma

        Returns
        -------
        object | None
            El dato del primer nodo en la cola y None cuando la cola no
            contenga nodos/datos
        """
        if not self.es_vacia():
            return self.__fre.dato
        return None

    def __len__(self):
        """Método que retorna del número de nodos que contiene la cola

        Returns
        -------
        int
            Tamaño de la cola
        """
        if self.es_vacia():
            return 0
        nodo = self.__fre
        cont = 0
        while nodo is not None:
            cont += 1
            nodo = nodo.siguiente
        return cont

    def __str__(self):
        """Método especial encargado de retornar una cadena con los datos
        actuales que se encuentran en la cola

        Returns
        -------
        str
            Una cadena que muestre todos los datos que actualmente almacena
            la cola, en el siguiente formato:
            "🏨🚶🚶🚶|[dato_0]| 👈 (dato_1) 👈 (dato_2) 👈 (dato_n)"
            Cuando hay un sólo dato:
            "🏨🚶🚶🚶#[dato_0]#"
            Cuando no hay datos:
            "🏨"
        """
        if self.es_vacia():
            return "🏨"
        nodo = self.__fre
        cadena = "🏨🚶🚶🚶"
        while nodo is not None:
            if nodo is self.__fre and nodo is self.__ter:
                cadena += f"#{nodo.dato}#"
            elif nodo is self.__fre:
                cadena += f"|{nodo.dato}|"
            else:
                cadena += f" 👈 ({nodo.dato})"
            nodo = nodo.siguiente
        return cadena
