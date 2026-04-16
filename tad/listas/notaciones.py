"""
prefija.py - Implementación de la notación prefija y su evaluación

Copyright (C) 2026 Ray
SPDX-License-Identifier: GPL-3.0-or-later
"""


from tad.listas.pila import Pila


class Prefija:  # Pregúnta a Chat-GPT cómo funciona 🫩
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
    def __init__(self, expresion_infija: str):
        self.__expr = expresion_infija
        self.__error = None

        try:
            self.__tokens = self.__tokenizar(self.__expr)
            self.__validar(self.__tokens)

        except ValueError as e:
            self.__tokens = []
            self.__error = str(e)
        except Exception:  # Manejo demasiado general
            self.__tokens = []
            self.__error = "Expresión inválida"

    def __tokenizar(self, expr: str):
        """Tokeniza y devuelve una cadena con tokens separados por espacios.
        Rechaza decimales y caracteres inválidos.
        """
        out = ""
        num = ""

        for ch in expr:
            if ch.isspace():
                if num:
                    out = (out + " " + num) if out else num
                    num = ""
                continue
            if ch.isdigit():
                num += ch
                continue
            if ch == ".":
                raise ValueError("Decimal no permitido")
            if num:
                out = (out + " " + num) if out else num
                num = ""
            if ch in "+-*/^()":
                out = (out + " " + ch) if out else ch
            else:
                raise ValueError("Carácter inválido")
        if num:
            out = (out + " " + num) if out else num
        return out

    def __validar(self, tokens_str: str):
        if not tokens_str:
            raise ValueError("Expresión vacía")
        balance = 0
        espera_operando = True

        for t in self.__iter_tokens_from_str(tokens_str):
            if t.isdigit():
                if not espera_operando:
                    raise ValueError("Operador mal ubicado")
                espera_operando = False
            elif t == "(":
                if not espera_operando:
                    raise ValueError("Operador mal ubicado")
                balance += 1
                espera_operando = True
            elif t == ")":
                if espera_operando:
                    raise ValueError("Operador mal ubicado")
                balance -= 1
                if balance < 0:
                    raise ValueError("Paréntesis desbalanceados")
                espera_operando = False
            elif t in "+-*/^":
                if espera_operando:
                    raise ValueError("Operador mal ubicado")
                espera_operando = True
            else:
                raise ValueError("Carácter inválido")

        if balance != 0:
            raise ValueError("Paréntesis desbalanceados")

        if espera_operando:
            raise ValueError("Expresión incompleta")

    def __iter_tokens_from_str(self, s: str):
        """Generador que recorre la cadena de tokens (separada por espacios)."""
        i = 0
        n = len(s)
        while i < n:
            if s[i].isspace():
                i += 1
                continue
            j = i
            while j < n and not s[j].isspace():
                j += 1
            yield s[i:j]
            i = j

    def in_fija(self):
        """Método que retorna la expresión Infija original, separando cada
        operando y cada operador, incluyendo los paréntesis, por un espacio
        en blanco.
        “(⬜12⬜-⬜8⬜)⬜^⬜3⬜+⬜7”
        """
        if self.__error:
            return self.__error
        return self.__tokens

    def __prec(self, op):
        if op == "^":
            return 3
        if op in "*/":
            return 2
        if op in "+-":
            return 1
        return 0

    def pre_fija(self):
        """Método que convierte una expresión Infija a una expresión Prefija,
        haciendo uso de una Pila. Separar operandos y operadores por un
        espacio en blanco.
        “+⬜^⬜-⬜12⬜8⬜3⬜7”
        """
        if self.__error:
            return self.__error

        ops = Pila()
        salida_pila = Pila()

        tokens_pila = Pila()
        for tok in self.__iter_tokens_from_str(self.__tokens):
            tokens_pila.apilar(tok)

        while not tokens_pila.es_vacia():
            t = tokens_pila.desapilar()
            if t == "(":
                t = ")"
            elif t == ")":
                t = "("

            if t.isdigit():
                salida_pila.apilar(t)
            elif t == "(":
                ops.apilar(t)
            elif t == ")":
                while not ops.es_vacia() and ops.cima() != "(":
                    salida_pila.apilar(ops.desapilar())
                if ops.es_vacia():
                    self.__error = "Paréntesis desbalanceados"
                    return self.__error
                ops.desapilar()
            else:
                while (
                    not ops.es_vacia()
                    and ops.cima() != "("
                    and (
                        self.__prec(ops.cima()) > self.__prec(t)
                        or (
                            self.__prec(ops.cima()) == self.__prec(t)
                            and t != "^"
                        )
                    )
                ):
                    salida_pila.apilar(ops.desapilar())
                ops.apilar(t)

        while not ops.es_vacia():
            top = ops.desapilar()
            if top in "()":
                self.__error = "Paréntesis desbalanceados"
                return self.__error
            salida_pila.apilar(top)

        res = ""
        while not salida_pila.es_vacia():
            tok = salida_pila.desapilar()
            res = (res + " " + tok) if res else tok
        return res

    def __tomar_operando(self, pila):
        val = pila.desapilar()
        if val is None:
            raise ValueError("Expresión inválida")
        return val

    def eval_expr_aritmetica(self):
        """Evaluación de la expresión aritmética en notación Prefija,
        utilizando una Pila, calculando el resultado final de la expresión."""
        if self.__error:
            return None

        prefija_str = self.pre_fija()
        if self.__error:
            return None

        pref_pila = Pila()
        for tok in self.__iter_tokens_from_str(prefija_str):
            pref_pila.apilar(tok)

        pila = Pila()
        while not pref_pila.es_vacia():
            t = pref_pila.desapilar()
            if t.isdigit():
                pila.apilar(float(t))
                continue
            if t not in "+-*/^":
                self.__error = "Operador inválido"
                return None
            a = self.__tomar_operando(pila)
            b = self.__tomar_operando(pila)
            if t == "+":
                pila.apilar(a + b)
            elif t == "-":
                pila.apilar(a - b)
            elif t == "*":
                pila.apilar(a * b)
            elif t == "/":
                if b == 0:
                    self.__error = "División por cero"
                    return None
                pila.apilar(a / b)
            elif t == "^":
                pila.apilar(a ** b)

        res = pila.desapilar()
        if res is None or not pila.es_vacia():
            self.__error = "Expresión inválida"
            return None
        return float(res)
