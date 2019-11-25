import unittest
from unittest.mock import patch
import baraja

def mi_eligecarta(i, longitud):
    if i == longitud-1:
     return 0
    else:
        return i+1

class BarajaTest(unittest.TestCase):

    def test_crear_baraja(self):
        b = baraja.baraja()
        self.assertEqual(len(b), 40)
        self.assertEqual(b, ['Ao', '2o', '3o', '4o', '5o', '6o', '7o', 'So', 'Co', 'Ro', 'Ac', '2c', '3c', '4c', '5c', '6c', '7c', 'Sc', 'Cc', 'Rc', 'Ae', '2e', '3e', '4e', '5e', '6e', '7e', 'Se', 'Ce', 'Re', 'Ab', '2b', '3b', '4b', '5b', '6b', '7b', 'Sb', 'Cb', 'Rb'])

        self.assertEqual(b[0], "Ao")
        self.assertEqual(b[39], "Rb")
        self.assertEqual(b[10], "Ac")
        self.assertEqual(b[20], "Ae")

    @patch("baraja.elige_carta", mi_eligecarta)
    def test_mezclar_lista(self):
        b = ["A", "B", "C", "D", "E"]
        mezclada = ["A", "C", "D", "E", "B"]
        b = baraja.mezclar(b)
        self.assertEqual(b, mezclada)



if __name__ == "__main__":
    unittest.main()
