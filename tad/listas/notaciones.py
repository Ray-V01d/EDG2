"""
prefija.py - Implementación de la notación prefija y su evaluación

Copyright (C) 2026 Ray
SPDX-License-Identifier: GPL-3.0-or-later
"""

from tad.listas.pila import Pila


class Prefija:
    """Clase que implementa la transformación de un expresión
    matemática Infija a Prefija (notación Polaca) y el cálculo
    de la expresión aritmética Prefija.
    Los operandos utilizados serán de cualquier cantidad de
    dígitos.
    Operadores Válidos:
    + : Suma
    - : Resta
    * : Multiplicación
    / : División
    ^ : Potenciación
    ( : Paréntesis Izquierdo
    ) : Paréntesis Derecho
    """
    def __init__(self, expresión_infija: str):
        """Inicializa la clase con una expresión infija"""
        self.__expresión_infija = expresión_infija
        self.__infija_formateada: None | str = None
        self.__prefija_result: None | str = None

    def __precedencia(self, operador: str) -> int:
        if operador == '^':
            return 3
        elif operador in ['*', '/']:
            return 2
        elif operador in ['+', '-']:
            return 1
        return 0

    def __es_operador(self, car: str) -> bool:
        return car in ['+', '-', '*', '/', '^']

    def __es_dígito(self, car: str) -> bool:
        return car.isdigit()

    def in_fija(self) -> str:
        """Método que retorna la expresión Infija original, separando cada
        operando y cada operador, incluyendo los paréntesis, por un espacio
        en blanco.
        "(⬜12⬜-⬜8⬜)⬜^⬜3⬜+⬜7"
        """
        try:
            if self.__infija_formateada is not None:
                return self.__infija_formateada
            resultado = ""
            i = 0
            expr = self.__expresión_infija

            while i < len(expr):
                car = expr[i]
                if car == ' ':
                    i += 1
                    continue
                if self.__es_dígito(car):
                    operando = ""
                    while i < len(expr) and self.__es_dígito(expr[i]):
                        operando += expr[i]
                        i += 1
                    if resultado:
                        resultado += " "
                    resultado += operando
                    continue
                if self.__es_operador(car) or car in ['(', ')']:
                    if resultado:
                        resultado += " "
                    resultado += car
                    i += 1
                    continue
                i += 1

            self.__infija_formateada = resultado
            return self.__infija_formateada
        except Exception:
            return ""

    def pre_fija(self) -> str:
        """Método que convierte una expresión Infija a una expresión Prefija,
        haciendo uso de una Pila. Separar operandos y operadores por un
        espacio en blanco.
        "+⬜^⬜-⬜12⬜8⬜3⬜7"
        """
        try:
            infija_fmt = self.in_fija()
            expr_invertida = ""
            i = len(infija_fmt) - 1

            while i >= 0:
                if infija_fmt[i] == '(':
                    expr_invertida += ')'
                    i -= 1
                elif infija_fmt[i] == ')':
                    expr_invertida += '('
                    i -= 1
                else:
                    expr_invertida += infija_fmt[i]
                    i -= 1
            postfija_invertida = self.__infija_a_postfija(expr_invertida)
            prefija = ""
            i = len(postfija_invertida) - 1

            while i >= 0:
                prefija += postfija_invertida[i]
                i -= 1
            self.__prefija_result = prefija
            return self.__prefija_result
        except Exception:
            return ""

    def __infija_a_postfija(self, infija: str) -> str:
        """Convierte una expresión infija a postfija usando una pila
        Algoritmo de Dijkstra (Shunting Yard)
        """
        try:
            pila_operadores = Pila()
            resultado = ""
            tokens = infija.split()

            for token in tokens:
                if self.__es_dígito(token[0]):
                    if resultado:
                        resultado += " "
                    resultado += token
                elif token == '(':
                    pila_operadores.apilar(token)
                elif token == ')':
                    while not pila_operadores.es_vacia() and pila_operadores.cima() != '(':
                        op = pila_operadores.desapilar()
                        if resultado:
                            resultado += " "
                        resultado += op
                    pila_operadores.desapilar()
                elif self.__es_operador(token):
                    if token == '^':
                        while (not pila_operadores.es_vacia() and
                               pila_operadores.cima() != '(' and
                               self.__precedencia(pila_operadores.cima()) > self.__precedencia(token)):
                            op = pila_operadores.desapilar()
                            if resultado:
                                resultado += " "
                            resultado += op
                    else:
                        while (not pila_operadores.es_vacia() and
                               pila_operadores.cima() != '(' and
                               self.__precedencia(pila_operadores.cima()) >= self.__precedencia(token)):
                            op = pila_operadores.desapilar()
                            if resultado:
                                resultado += " "
                            resultado += op
                    pila_operadores.apilar(token)

            while not pila_operadores.es_vacia():
                op = pila_operadores.desapilar()
                if resultado:
                    resultado += " "
                resultado += op

            return resultado
        except Exception:
            return ""

    def eval_expr_aritmetica(self) -> float:
        """Evaluación de la expresión aritmética en notación Prefija,
        utilizando una Pila, calculando el resultado final de la expresión."""
        try:
            prefija = self.pre_fija()
            tokens = prefija.split()
            pila_datos = Pila()
            i = len(tokens) - 1

            while i >= 0:
                token = tokens[i]
                if self.__es_dígito(token[0]):
                    pila_datos.apilar(float(token))
                elif self.__es_operador(token):
                    operando1 = pila_datos.desapilar()
                    operando2 = pila_datos.desapilar()
                    if token == '+':
                        resultado = operando1 + operando2
                    elif token == '-':
                        resultado = operando1 - operando2
                    elif token == '*':
                        resultado = operando1 * operando2
                    elif token == '/':
                        resultado = operando1 / operando2
                    elif token == '^':
                        resultado = operando1 ** operando2
                    pila_datos.apilar(resultado)
                i -= 1
            resultado = pila_datos.desapilar()
            return resultado if resultado is not None else 0.0
        except Exception:
            return 0.0
