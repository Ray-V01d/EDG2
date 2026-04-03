# Proyecto de Estructuras de Datos (EDG2)

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

> Una colección didáctica de implementaciones clásicas de estructuras de datos en Python, pensada para aprendizaje, pruebas de conceptos y trabajo académico.

---

## 🚀 Descripción

Este proyecto incluye implementaciones propias y pruebas de:

- Listas enlazadas simples (LSE)
- Pilas (stack)
- Colas (queue)
- Lista de cadenas simples extendidas (LCSE)
- Nodos genéricos para estructuras enlazadas

Todos los módulos están en `tad/listas/` y se prueban con archivos `test_*.py`.

## 📁 Estructura del proyecto

- `tad/` - paquete principal
  - `listas/` - implementaciones de estructuras
    - `lse.py`
    - `pila.py`
    - `cola.py`
    - `lcse.py`
    - `nodos.py`
- `test_lse.py`, `test_lcse.py`, `test_nodos.py` - pruebas unitarias
- `README.md` - documentación del proyecto

## 🛠️ Instalación

Clonar el repositorio:

```bash
git clone https://github.com/Ray-V01d/EDG2.git
cd EDG2
```

## 🧪 Ejecución de pruebas

(En construcción)


## 📌 Uso básico

Ejemplo mínimo usando `LSE` (Lista Simple Enlazada):

```python
from tad.listas.lse import ListaSimplementeEnlazada

lista = ListaSimplementeEnlazada()
lista.agregar(10)
lista.agregar(20)
lista.agregar(30)
lista.agregar(40)
print(lista)
```

> Ajusta el ejemplo al API de tu implementación actual.

## 🤝 Contribuciones

(En construcción)

## 📜 Licencia

GNU GPLv3.0. Revisa `LICENSE` para detalles.

