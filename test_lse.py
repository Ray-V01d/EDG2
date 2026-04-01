from tad.listas.lse import ListaSimplementeEnlazada

if __name__ == "__main__":
    lst_nums = ListaSimplementeEnlazada()
    lst_nums.agregar(0)  # *** DETERMINA EL TIPO DE DATO DE LA LISTA ***
    lst_nums.agregar(1)
    lst_nums.agregar(2)
    lst_nums.agregar(3)
    lst_nums.agregar(4)

    lst_nums.explorar()

    """print(lst_nums.buscar(17))
    print(f'El dato en la posición es {lst_nums.buscar(1, False)}')"""

    lst_nums.insertar(512, -1)
    lst_nums.insertar(512)
    lst_nums.insertar(64)
    lst_nums.insertar("u", 1)
    lst_nums.insertar(98, 3)
    lst_nums.insertar(42, 6)
    print('+--------------------------------------+')
    lst_nums.explorar()
