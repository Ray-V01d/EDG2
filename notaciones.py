"""
prefija.py - Implementación de una clase para manejar expresiones en notación prefija

Copyright (C) 2026 Ray
SPDX-License-Identifier: GPL-3.0-or-later
"""

class Prefija:


    def __init__(self, expresión_infija:str):
    
    
    def in_fija(self):
        Método que retorna la expresión Infija original, separando cada
        operando y cada operador, incluyendo los paréntesis, por un espacio
        en blanco.
        “( 12 - 8 ) ^ 3 + 7”⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜
    
    def pre_fija(self):
    Método que convierte una expresión Infija a una expresión Prefija,
    haciendo uso de una Pila. Separar operandos y operadores por un
    espacio en blanco.
    “+ ^ - 12 8 3 7”⬜ ⬜ ⬜ ⬜ ⬜ ⬜

    def eval_expr_aritmetica(self):
        Evaluación de la expresión aritmética en notación Prefija,
        utilizando una Pila, calculando el resultado final de la expresión.