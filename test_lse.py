"""
Módulo de pruebas para la clase ListaSimplementeEnlazada.

Autor: Ray
Año: 2026
Licencia: GNU GPL v2.0
"""


from tad.listas.lse import ListaSimplementeEnlazada


def main():
    lista = ListaSimplementeEnlazada()

    # ---------------- Agregar ----------------
    print("Agregar elementos:")
    lista.agregar(1)
    lista.agregar(3)
    lista.agregar(5)
    lista.agregar(7)
    lista.agregar('x')
    lista.explorar()
    print("---------------------------------------------")
    # ---------------- Insertar ----------------
    print("Insertar elementos:")
    lista.insertar(0, 0)
    lista.insertar(3, 3)
    lista.insertar(9, len(lista))
    lista.insertar(100, 999)
    lista.insertar('y', 2)
    lista.explorar()
    print("---------------------------------------------")
    # ---------------- Suprimir por dato ----------------
    print("Suprimir por dato:")
    lista.suprimir(10, True)
    lista.suprimir(40, True)
    lista.suprimir(999, True)
    lista.suprimir(20, True)
    lista.suprimir(30, True)
    lista.explorar()
    print("---------------------------------------------")
    # ---------------- Suprimir por posición ----------------
    print("Suprimir por posición:")
    lista.suprimir(0, False)
    lista.suprimir(1, False)
    lista.suprimir(len(lista) - 1, False)
    lista.suprimir(-1, False)
    lista.suprimir(999, False)
    lista.explorar()
    print("---------------------------------------------")
    # ---------------- Buscar ----------------
    print("Buscar elementos:")
    lista.buscar(200)
    lista.buscar(999)
    lista.buscar(1, False)
    lista.buscar(3, False)
    lista.explorar()
    print("---------------------------------------------")
    # ---------------- getitem ----------------
    print("Elemento en posición 0:", lista[0])
    print("Elemento en posición 2:", lista[2])
    try:
        print("Elemento en posición 999:", lista[999])
    except IndexError as e:
        print("Error:", e)
    print("---------------------------------------------")
    # ---------------- len, es_vacia, iter ----------------
    print("Longitud de la lista:", len(lista))
    print("---------------------------------------------")
    print("¿Está vacía?", lista.es_vacia())
    print("---------------------------------------------")
    for elemento in lista:
        print("elemento:", elemento)
    print("---------------------------------------------")
    while not lista.es_vacia():
        lista.suprimir(0, False)
        print(lista)
    print("---------------------------------------------")
    print("Lista final (explorar):")
    lista.explorar()
    print("Lista final (str):")
    print(lista)
    print("---------------------------------------------")


if __name__ == "__main__":
    main()
