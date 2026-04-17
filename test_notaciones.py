"""
test_notaciones.py - Test suite para la clase Prefija
"""

from tad.listas.notaciones import Prefija


def test_basico():
    """Pruebas básicas"""
    print("\nPRUEBAS BÁSICAS")
    print("=" * 60)
    casos = [
        ("2+3", 5.0),
        ("2-3", -1.0),
        ("2*3", 6.0),
        ("10/2", 5.0),
        ("2^3", 8.0),
    ]
    for expr, esperado in casos:
        p = Prefija(expr)
        resultado = p.eval_expr_aritmetica()
        estado = "✓" if abs(resultado - esperado) < 0.001 else "✗"
        print(f"{estado} {expr:15} → {resultado}")


def test_precedencia():
    """Pruebas de precedencia de operadores"""
    print("\nPRECEDENCIA DE OPERADORES")
    print("=" * 60)
    casos = [
        ("2+3*4", 14.0),
        ("2*3+4", 10.0),
        ("10/2+3", 8.0),
        ("2^3*2", 16.0),
    ]
    for expr, esperado in casos:
        p = Prefija(expr)
        resultado = p.eval_expr_aritmetica()
        estado = "✓" if abs(resultado - esperado) < 0.001 else "✗"
        print(f"{estado} {expr:15} → {resultado}")


def test_parentesis():
    """Pruebas con paréntesis"""
    print("\nPARÉNTESIS")
    print("=" * 60)
    casos = [
        ("(2+3)", 5.0),
        ("(2+3)*4", 20.0),
        ("2*(3+4)", 14.0),
        ("(2+3)*(4+5)", 45.0),
    ]
    for expr, esperado in casos:
        p = Prefija(expr)
        resultado = p.eval_expr_aritmetica()
        estado = "✓" if abs(resultado - esperado) < 0.001 else "✗"
        print(f"{estado} {expr:20} → {resultado}")


def test_operandos_multiples():
    """Pruebas con operandos de múltiples dígitos"""
    print("\nOPERANDOS MÚLTIPLES DÍGITOS")
    print("=" * 60)
    casos = [
        ("12+34", 46.0),
        ("123*45", 5535.0),
        ("1000/10", 100.0),
        ("12345+54321", 66666.0),
    ]
    for expr, esperado in casos:
        p = Prefija(expr)
        resultado = p.eval_expr_aritmetica()
        estado = "✓" if abs(resultado - esperado) < 0.001 else "✗"
        print(f"{estado} {expr:20} → {resultado}")


def test_complejas():
    """Pruebas complejas"""
    print("\nEXPRESIONES COMPLEJAS")
    print("=" * 60)
    casos = [
        ("(12-8)^3+7", 71.0),
        ("0-3*(4+5)", -27.0),
        ("2+3*4-5", 9.0),
        ("10/2+3*4", 17.0),
    ]
    for expr, esperado in casos:
        p = Prefija(expr)
        resultado = p.eval_expr_aritmetica()
        estado = "✓" if abs(resultado - esperado) < 0.001 else "✗"
        print(f"{estado} {expr:20} → {resultado}")


def test_formato():
    """Pruebas de formato infija y prefija"""
    print("\nFORMATO INFIJA Y PREFIJA")
    print("=" * 60)
    casos = [
        ("2+3", "2 + 3", "+ 2 3"),
        ("(2+3)*4", "( 2 + 3 ) * 4", "* + 2 3 4"),
        ("2^3+1", "2 ^ 3 + 1", "+ ^ 2 3 1"),
    ]
    for expr, infija_exp, prefija_exp in casos:
        p = Prefija(expr)
        infija = p.in_fija()
        prefija = p.pre_fija()
        est_inf = "✓" if infija == infija_exp else "✗"
        est_pre = "✓" if prefija == prefija_exp else "✗"
        print(f"{est_inf} Infija  : {expr:10} → {infija}")
        print(f"{est_pre} Prefija : {expr:10} → {prefija}")


def test_errores():
    """Pruebas de casos problemáticos (sin excepciones)"""
    print("\nCASOS PROBLEMÁTICOS (SIN EXCEPCIONES)")
    print("=" * 60)
    casos = [
        ("", "Vacío"),
        ("10/0", "División por cero"),
        ("-3+4", "Operador unario"),
        ("5+*3", "Operadores inválidos"),
        ("((2+3)", "Paréntesis desbalanceados"),
        ("abc", "Caracteres inválidos"),
    ]
    for expr, desc in casos:
        try:
            p = Prefija(expr)
            resultado = p.eval_expr_aritmetica()
            print(f"✓ {desc:25} → {resultado}")
        except Exception as e:
            print(f"✗ {desc:25} → EXCEPCIÓN: {type(e).__name__}")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("TEST SUITE - CLASE PREFIJA".center(60))
    print("=" * 60)
    
    test_basico()
    test_precedencia()
    test_parentesis()
    test_operandos_multiples()
    test_complejas()
    test_formato()
    test_errores()
    
    print("\n" + "=" * 60)
    print("FIN DE LAS PRUEBAS".center(60))
    print("=" * 60 + "\n")
