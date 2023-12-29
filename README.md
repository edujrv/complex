
# Complejo - Clase para Números Complejos en Python

La clase `Complejo` proporciona una implementación en Python para trabajar con números complejos. Esta implementación sigue el paradigma de programación funcional y se esfuerza por mantener la inmutabilidad de los objetos `Complejo`.

## Características Principales

- **Operaciones Aritméticas:** Soporte para suma, resta, multiplicación y división de números complejos.
- **Operadores de Comparación:** Implementación de operadores de comparación (`==`, `>`, `<`, `>=`, `<=`, `!=`) con la capacidad de comparar con números complejos, enteros y flotantes.
- **Métodos Adicionales:** Funciones útiles como cálculo del conjugado, fase, inverso, etc.
- **Entrada desde Cadena de Texto:** Método para crear instancias `Complejo` a partir de cadenas de texto.

## Uso Básico

```python
# Crear números complejos
c1 = Complejo(2, 3)
c2 = Complejo(-1, 4)

# Realizar operaciones
suma = c1 + c2
resta = c1 - c2
multiplicacion = c1 * c2
division = c1 / c2

# Comparaciones
igual = c1 == c2
mayor_que = c1 > c2

# Métodos adicionales
conjugado_c1 = c1.conjugado()
fase_c1 = c1.fase()
inverso_c1 = c1.inverso()
```
## Contexto

Esta implementacion fue desarrollada como parte del examen final de programacion funcional. Su diseño y funcionalidades refrejan los principios aprendidos durante el cursado.

## Requisitos

- Python 3.6 o superior