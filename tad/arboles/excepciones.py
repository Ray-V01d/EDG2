class DuplicatedKeyError(Exception):
    """Excepción que se lanza cuando se intenta insertar una clave duplicada en el árbol."""
    def __init__(self, clave):
        super().__init__(f"La clave [{clave}] se encuentra DUPLICADA.")