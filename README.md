# Proyecto de Estructuras de Datos (EDG2)

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-GPLv3-blue)

> Una colección de implementaciones clásicas de estructuras de datos en Python, trabajo académico.

---

## 📌 Contenido

- [Descripción](#-descripción)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Instalación](#-instalación)
- [Ejecución de pruebas](#-ejecución-de-pruebas)
- [Uso básico](#-uso-básico)
- [Contribuciones](#-contribuciones)
- [Licencia](#-licencia)

## 🚀 Descripción

Este proyecto incluye implementaciones propias y pruebas de:

- Listas enlazadas simples (LSE)
- Lista de circulares simplemente enlazadas (LCSE)
- Pilas (stack)
- Colas (queue)
- Nodos genéricos para estructuras enlazadas

Todos los módulos están en `tad/listas/` y se prueban con archivos `test_*.py`.

## 📁 Estructura del proyecto

- `tad/` - paquete principal
  - `listas/` - implementaciones de estructuras:
    - `lse.py`
    - `pila.py`
    - `cola.py`
    - `lcse.py`
    - `nodos.py`
- `test_lse.py`, `test_lcse.py`, `test_nodos.py` - pruebas unitarias
- `README.md` - documentación del proyecto
- `LICENSE` - licencia

## 🛠️ Instalación

1. Clonar el repositorio

```bash
git clone https://github.com/Ray-V01d/EDG2.git
cd EDG2
```

## 🧪 Ejecución de pruebas

(En construcción)

## 📌 Uso básico

Ejemplo mínimo usando `ListaSimplementeEnlazada` (LSE):

```python
from tad.listas.lse import ListaSimplementeEnlazada

lista = ListaSimplementeEnlazada()
lista.agregar(10)
lista.agregar(20)
lista.agregar(30)
lista.agregar(40)
print(lista)
```

### Ejemplo de operaciones adicionales

```python
print(len(lista))               # salida esperada: 4
print(lista.buscar(20))         # 20
print(lista.buscar(2, por_dato=False))  # 30 (índice 2)
lista.insertar(5, 0)
lista.suprimir(10)
print(lista)
```

## 🤝 Contribuciones

(En construcción)

## 📜 Licencia

GNU GPLv3.0. Revisa `LICENSE` para detalles.


