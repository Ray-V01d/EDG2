"""
pila.py - Implementación de una pila de datos

Copyright (C) 2026 Ray
SPDX-License-Identifier: GPL-3.0-or-later
"""


from tad.listas.nodos import NodoListaSimplementeEnlazada as NLSE


class Pila:
    """Clase que implementa el funcionamiento del TAD Pila
    """
    def __init__(self):
        """Método constructor que realiza la creación e inicialización de
        una Pila
        """
        self.__cima = None

    def es_vacia(self):
        """Método que verifica si la pila se encuentra vacía

        Returns
        -------
        bool
            Retorna True si la pila es vacia. False en caso contrario
        """
        return self.__cima is None

    def homogeneo(self, new_dat):
        """Método que valida homogeneidad

        Parameters
        ----------
        new_dat : object
            El nuevo dato a validar

        Returns
        -------
        bool
            True si new_dat es del mismo tipo que los datos de la pila
            False en caso contrario
        """
        if self.es_vacia():
            return True
        return type(new_dat) is type(self.__cima.dato)

    def apilar(self, nuevo_dato):
        """Método que realiza la entrada de un nuevo dato a la pila.
        Realizar la validación de Homogeneidad para cada dato ingresado
        a la pila

        Parameters
        ----------
        nuevo_dato : object
        El nuevo dato a ser adicionado a la pila

        Returns
        -------
        bool
            True si nuevo_dato fue apilado. False en caso contrario
        """
        if self.homogeneo(nuevo_dato):
            new_nod = NLSE(nuevo_dato)
            new_nod.sig = self.__cima
            self.__cima = new_nod
            return True
        return False

    def desapilar(self):
        """Método que saca/quita el último nodo (elimina el nodo) de la pila
        y retorna su dato

        Returns
        -------
        object | None
            El dato del nodo desapilado y None cuando la pila no contenga
            nodos/datos
        """
        if self.es_vacia():
            return None
        dat = self.__cima.dato
        self.__cima = self.__cima.sig
        return dat

    def cima(self):
        """Método que retorna el dato del último nodo ingresado en la pila,
        sin quitarlo de la misma

        Returns
        -------
        object | None
            El dato del último nodo ingresado y None cuando la pila no
            contenga nodos/datos
        """
        if self.es_vacia():
            return None
        return self.__cima.dato

    def __len__(self):
        """Método que retorna el número de nodos que contiene la pila

        Returns
        -------
        int
            Tamaño de la pila
        """
        count = 0
        act = self.__cima
        while act is not None:
            count += 1
            act = act.sig
        return count

    def __str__(self):
        """Método especial encargado de retornar una cadena con los datos
        actuales que se encuentran en la pila (sin desapilarlos)

        Returns
        -------
        str
            Una cadena que muestre todos los datos que actualmente almacena
            la pila, en el siguiente formato:
            “🔝[dato_n] 🔜 [dato_3] 🔜 [dato_2] 🔜 [dato_1]”
            Cuando hay un sólo dato:
            “🔝[dato_1]”
            Cuando no hay datos:
            “🔝”
        """
        if self.es_vacia():
            return "🔝"
        act = self.__cima
        out = "🔝"
        while act is not None:
            out += f"[{act.dato}]"
            if act.sig is not None:
                out += " 🔜 "
            act = act.sig
        return out
