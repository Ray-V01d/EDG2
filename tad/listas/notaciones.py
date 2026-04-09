"""
prefija.py - Implementación de la notación prefija y su evaluación

Copyright (C) 2026 Ray
SPDX-License-Identifier: GPL-3.0-or-later
"""


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
        pass

    def in_fija(self) -> str:
        """Método que retorna la expresión Infija original, separando cada
        operando y cada operador, incluyendo los paréntesis, por un espacio
        en blanco.
        “(⬜12⬜-⬜8⬜)⬜^⬜3⬜+⬜7”
        """
        return

    def pre_fija(self) -> str:
        """Método que convierte una expresión Infija a una expresión Prefija,
        haciendo uso de una Pila. Separar operandos y operadores por un
        espacio en blanco.
        “+⬜^⬜-⬜12⬜8⬜3⬜7”
        """
        return

    def eval_expr_aritmetica(self) -> float:
        """Evaluación de la expresión aritmética en notación Prefija,
        utilizando una Pila, calculando el resultado final de la expresión."""
        return
