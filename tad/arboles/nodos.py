class NodoArbolBinario:
    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None

    def tiene_hijos(self):
        if self.izq or self.der:
            return True
        return False

    def __str__(self):
        return f"{self.clave}"
