import unittest
from Complejo import Complejo

class TestComplejo(unittest.TestCase):
    def test_suma(self):
        c1 = Complejo(2, 3)
        c2 = Complejo(4, 5)
        i1 = 2
        f1 = 3.5
        # Suma de dos complejos
        resultado = c1 + c2
        self.assertEqual(resultado.real, 6)
        self.assertEqual(resultado.imaginario, 8)

        # Suma de un complejo y un entero
        resultado = c1 + i1
        self.assertEqual(resultado.real, 4)
        self.assertEqual(resultado.imaginario, 3)

        # Suma de un complejo y un flotante
        resultado = c1 + f1
        self.assertEqual(resultado.real, 5.5)
        self.assertEqual(resultado.imaginario, 3)

        # Suma de un entero y un complejo
        resultado = i1 + c1
        self.assertEqual(resultado.real, 4)
        self.assertEqual(resultado.imaginario, 3)

        # Suma de un flotante y un complejo
        resultado = f1 + c1
        self.assertEqual(resultado.real, 5.5)
        self.assertEqual(resultado.imaginario, 3)


    def test_resta(self):
        c1 = Complejo(2, 3)
        c2 = Complejo(4, 5)
        i1 = 2
        f1 = 3.5

        # Resta de dos complejos
        resultado = c1 - c2
        self.assertEqual(resultado.real, -2)
        self.assertEqual(resultado.imaginario, -2)

        # Resta de un complejo y un entero
        resultado = c1 - i1
        self.assertEqual(resultado.real, 0)
        self.assertEqual(resultado.imaginario, 3)

        # Resta de un complejo y un flotante
        resultado = c1 - f1
        self.assertEqual(resultado.real, -1.5)
        self.assertEqual(resultado.imaginario, 3)

        # Resta de un entero y un complejo
        resultado = i1 - c1
        self.assertEqual(resultado.real, 0)
        self.assertEqual(resultado.imaginario, -3)

        # Resta de un flotante y un complejo
        resultado = f1 - c1
        self.assertEqual(resultado.real, 1.5)
        self.assertEqual(resultado.imaginario, -3)


    def test_multiplicacion(self):
        c1 = Complejo(2, 3)
        c2 = Complejo(4, 5)
        i1 = 2
        f1 = 3.5

        # Multiplicacion de dos complejos
        resultado = c1 * c2
        self.assertEqual(resultado.real, -7)
        self.assertEqual(resultado.imaginario, 22)

        # Multiplicacion de un complejo y un entero
        resultado = c1 * i1
        self.assertEqual(resultado.real, 4)
        self.assertEqual(resultado.imaginario, 6)

        # Multiplicacion de un complejo y un flotante
        resultado = c1 * f1
        self.assertEqual(resultado.real, 7)
        self.assertEqual(resultado.imaginario, 10.5)

        # Multiplicacion de un entero y un complejo
        resultado = i1 * c1
        self.assertEqual(resultado.real, 4)
        self.assertEqual(resultado.imaginario, 6)

        # Multiplicacion de un flotante y un complejo
        resultado = f1 * c1
        self.assertEqual(resultado.real, 7)
        self.assertEqual(resultado.imaginario, 10.5)


    def test_division(self):
        c1 = Complejo(2, 3)
        c2 = Complejo(4, 5)
        i1 = 2
        f1 = 3.5

        # Division de dos complejos
        resultado = c1 / c2
        self.assertAlmostEqual(resultado.real, 0.56, places=2)
        self.assertAlmostEqual(resultado.imaginario, 0.048, places=2)

        # Division de un complejo y un entero
        resultado = c1 / i1
        self.assertEqual(resultado.real, 1)
        self.assertEqual(resultado.imaginario, 1.5)

        # Division de un complejo y un flotante
        resultado = c1 / f1
        self.assertAlmostEqual(resultado.real, 0.57, places=2)
        self.assertAlmostEqual(resultado.imaginario, 0.857, places=2)

        # Division de un entero y un complejo
        resultado = i1 / c1
        self.assertAlmostEqual(resultado.real, 0.31, places=2)
        self.assertAlmostEqual(resultado.imaginario, -0.46, places=2)

        # Division de un flotante y un complejo
        resultado = f1 / c1
        self.assertAlmostEqual(resultado.real, 0.54, places=2)
        self.assertAlmostEqual(resultado.imaginario, -0.81, places=2)

    def test_potencia(self):
        c = Complejo(2, 3)

        # Potencia de un complejo con n positivo
        resultado = c ** 2
        self.assertAlmostEqual(resultado.real, -5, places=2)
        self.assertAlmostEqual(resultado.imaginario, 12, places=2)

        # Potencia de un complejo con n negativo
        resultado = c ** -2
        self.assertAlmostEqual(resultado.real, -0.029, places=2)
        self.assertAlmostEqual(resultado.imaginario, -0.071, places=2)

        # Potencia de un complejo con n=0
        resultado = c ** 0
        self.assertAlmostEqual(resultado.real, 1, places=2)
        self.assertAlmostEqual(resultado.imaginario, 0, places=2)

        # Potencia de un complejo con n=1
        resultado = c ** 1
        self.assertAlmostEqual(resultado.real, 2, places=2)
        self.assertAlmostEqual(resultado.imaginario, 3, places=2)

    def test_negativo(self):
        c = Complejo(2, 3)

        # Negativo de un complejo
        resultado = -c
        self.assertEqual(resultado.real, -2)
        self.assertEqual(resultado.imaginario, -3)

        # Negativo de un complejo negativo
        resultado = -resultado
        self.assertEqual(resultado.real, 2)
        self.assertEqual(resultado.imaginario, 3)

    def test_modulo(self):
        # Modulo de un complejo positivo
        c = Complejo(3, 4)
        resultado = abs(c)
        self.assertAlmostEqual(resultado, 5, places=2)

        # Modulo de un complejo negativo
        c = Complejo(-3, -4)
        resultado = abs(c)
        self.assertAlmostEqual(resultado, 5, places=2)


    def test_igualdad(self):
        # Igualdad de dos complejos iugales
        c1 = Complejo(2, 3)
        c2 = Complejo(2, 3)
        self.assertTrue(c1 == c2)

        # Igualdad de dos complejos distintos
        c1 = Complejo(2, 3)
        c2 = Complejo(2, -3)
        self.assertFalse(c1 == c2)

        c1 = Complejo(2, 3)
        c2 = Complejo(-2, 3)
        self.assertFalse(c1 == c2)

        c1 = Complejo(2, -3)
        c2 = Complejo(-2, 3)
        self.assertFalse(c1 == c2)

        # Igualdad de un complejo y un entero
        c1 = Complejo(2, 0)
        c2 = 2
        self.assertTrue(c1 == c2)

        c1 = Complejo(-2, 0)
        c2 = 2
        self.assertFalse(c1 == c2)

        c1 = Complejo(2, -1)
        c2 = 2
        self.assertFalse(c1 == c2)

        # Igualdad de un complejo y un flotante
        c1 = Complejo(2.3, 0)
        c2 = 2.3
        self.assertTrue(c1 == c2)

        c1 = Complejo(-2, 0)
        c2 = 2.3
        self.assertFalse(c1 == c2)

        c1 = Complejo(2.8, -1)
        c2 = 2.1
        self.assertFalse(c1 == c2)


    def test_distinto(self):
        # Distinto de dos complejos distintos
        c1 = Complejo(2, 3)
        c2 = Complejo(2, -3)
        self.assertTrue(c1 != c2)

        c1 = Complejo(2, 3)
        c2 = Complejo(-2, 3)
        self.assertTrue(c1 != c2)

        # Distinto de dos complejos iguales
        c1 = Complejo(2, 3)
        c2 = Complejo(2, 3)
        self.assertFalse(c1 != c2)

        # Distinto de un complejo y un entero
        c1 = Complejo(2, 0)
        c2 = 2
        self.assertFalse(c1 != c2)

        c1 = Complejo(-2, 0)
        c2 = 2
        self.assertTrue(c1 != c2)

        c1 = Complejo(2, -1)
        c2 = 2
        self.assertTrue(c1 != c2)

        # Distinto de un complejo y un flotante
        c1 = Complejo(2.3, 0)
        c2 = 2.3
        self.assertFalse(c1 != c2)

        c1 = Complejo(-2, 0)
        c2 = 2.3
        self.assertTrue(c1 != c2)

        c1 = Complejo(2.8, -1)
        c2 = 2.1
        self.assertTrue(c1 != c2)


    def test_mayor_que(self):
        # Mayor que de dos complejos
        c1 = Complejo(2, 3)
        c2 = Complejo(1, 2)
        self.assertTrue(c1 > c2)

        c1 = Complejo(-2, 3)
        c2 = Complejo(1, 2)
        self.assertFalse(c1 > c2)

        # Mayor que de un complejo y un entero
        c1 = Complejo(2, 0)
        c2 = 1
        self.assertTrue(c1 > c2)

        c1 = Complejo(1, -1)
        c2 = 1
        self.assertFalse(c1 > c2)

        c1 = Complejo(1, 1)
        c2 = 1
        self.assertTrue(c1 > c2)

        # Mayor que de un complejo y un flotante
        c1 = Complejo(2.3, 0)
        c2 = 2.2
        self.assertTrue(c1 > c2)

        c1 = Complejo(1.1, -1)
        c2 = 1.1
        self.assertFalse(c1 > c2)

        c1 = Complejo(1.1, 1)
        c2 = 1.1
        self.assertTrue(c1 > c2)

        
    def test_menor_que(self):
        # Menor que de dos complejos
        c1 = Complejo(2, 3)
        c2 = Complejo(3, 4)
        self.assertTrue(c1 < c2)

        c1 = Complejo(-2, 3)
        c2 = Complejo(1, 2)
        self.assertTrue(c1 < c2)

        # Menor que de un complejo y un entero
        c1 = Complejo(2, 0)
        c2 = 3
        self.assertTrue(c1 < c2)

        c1 = Complejo(1, -1)
        c2 = 1
        self.assertTrue(c1 < c2)

        c1 = Complejo(1, 1)
        c2 = 1
        self.assertFalse(c1 < c2)

        # Menor que de un complejo y un flotante
        c1 = Complejo(2.3, 0)
        c2 = 2.4
        self.assertTrue(c1 < c2)

        c1 = Complejo(1.1, -1)
        c2 = 1.1
        self.assertTrue(c1 < c2)

        c1 = Complejo(1.1, 1)
        c2 = 1.1
        self.assertFalse(c1 < c2)

    def test_mayor_o_igual_que(self):
        # Mayor o igual que de dos complejos
        c1 = Complejo(2, 3)
        c2 = Complejo(2, 3)
        self.assertTrue(c1 >= c2)

        c1 = Complejo(-2, 3)
        c2 = Complejo(1, 2)
        self.assertFalse(c1 >= c2)

        # Mayor o igual que de un complejo y un entero
        c1 = Complejo(2, 0)
        c2 = 2
        self.assertTrue(c1 >= c2)

        c1 = Complejo(1, -1)
        c2 = 1
        self.assertFalse(c1 >= c2)

        c1 = Complejo(1, 1)
        c2 = 1
        self.assertTrue(c1 >= c2)

        # Mayor o igual que de un complejo y un flotante
        c1 = Complejo(2.3, 0)
        c2 = 2.3
        self.assertTrue(c1 >= c2)

        c1 = Complejo(1.1, -1)
        c2 = 1.1
        self.assertFalse(c1 >= c2)

        c1 = Complejo(1.1, 1)
        c2 = 1.1
        self.assertTrue(c1 >= c2)

    def test_menor_o_igual_que(self):
        # Menor o igual que de dos complejos
        c1 = Complejo(2, 3)
        c2 = Complejo(3, 4)
        self.assertTrue(c1 <= c2)

        c1 = Complejo(-2, 3)
        c2 = Complejo(1, 2)
        self.assertTrue(c1 <= c2)

        # Menor o igual que de un complejo y un entero
        c1 = Complejo(2, 0)
        c2 = 3
        self.assertTrue(c1 <= c2)

        c1 = Complejo(1, -1)
        c2 = 1
        self.assertTrue(c1 <= c2)

        c1 = Complejo(1, 1)
        c2 = 1
        self.assertFalse(c1 <= c2)

        # Menor o igual que de un complejo y un flotante
        c1 = Complejo(2.3, 0)
        c2 = 2.4
        self.assertTrue(c1 <= c2)

        c1 = Complejo(1.1, -1)
        c2 = 1.1
        self.assertTrue(c1 <= c2)

        c1 = Complejo(1.1, 1)
        c2 = 1.1
        self.assertFalse(c1 <= c2)

        c1 = Complejo(1.1, 0)
        c2 = 1.1
        self.assertTrue(c1 <= c2)

    def test_abs(self):
        c = Complejo(3, 4)
        resultado = abs(c)
        self.assertAlmostEqual(resultado, 5, places=2)

        c = Complejo(-3, -4)
        resultado = abs(c)
        self.assertAlmostEqual(resultado, 5, places=2)


    def test_conjugado(self):
        c = Complejo(2, 3)
        resultado = c.conjugado()
        self.assertEqual(resultado.real, 2)
        self.assertEqual(resultado.imaginario, -3)

        c = Complejo(-2, -3)
        resultado = c.conjugado()
        self.assertEqual(resultado.real, -2)
        self.assertEqual(resultado.imaginario, 3)

    def test_fase(self):
        c = Complejo(1, 1)
        resultado = c.fase()
        self.assertAlmostEqual(resultado, 0.79, places=2)

    def test_inverso(self):
        c = Complejo(2, 3)
        resultado = c.inverso()
        self.assertAlmostEqual(resultado.real, 0.153, places=2)
        self.assertAlmostEqual(resultado.imaginario, -0.23, places=2)

    def test_from_string(self):
        self.assertEqual(Complejo.from_string('3 + 2i'), Complejo(3, 2))
        self.assertEqual(Complejo.from_string('3 + 0i'), Complejo(3, 0))
        self.assertEqual(Complejo.from_string('3.3 + 2.0i'), Complejo(3.3, 2.0))
        self.assertEqual(Complejo.from_string('-3 + 2i'), Complejo(-3, 2))
        self.assertEqual(Complejo.from_string('-3 + i'), Complejo(-3, 1))
        self.assertEqual(Complejo.from_string('-3 - 2i'), Complejo(-3, -2))
        self.assertEqual(Complejo.from_string('-3 - i'), Complejo(-3, -1))
        self.assertEqual(Complejo.from_string('3 - 2i'), Complejo(3, -2))
        self.assertEqual(Complejo.from_string('3i'), Complejo(0, 3))
        self.assertEqual(Complejo.from_string('-3i'), Complejo(0, -3))
        self.assertEqual(Complejo.from_string('3'), Complejo(3, 0))
        self.assertEqual(Complejo.from_string('-3'), Complejo(-3, 0))
        self.assertEqual(Complejo.from_string('-i'), Complejo(0, -1))
        self.assertEqual(Complejo.from_string('i'), Complejo(0, 1))

if __name__ == '__main__':
    unittest.main()