"""UwU
"""


from tad.listas.notaciones import Prefija


if __name__ == "__main__":
    A = "(12-8)^3+7"
    B = "3+4*2/(B-5)^2^3"
    C = "12          34 +   5"
    infijas = [A, B, C]
    for i in infijas:
        prefija = Prefija(i)
        print(prefija.in_fija())

    print("-" * 79)
    # print(prefija.in_fija())
    # print(prefija.pre_fija())
