from mychar import cadena_mas_larga 
import unittest
import random
import string

class TestCadenaMasLarga(unittest.TestCase):


    def  test_lista_principal(self):
        lista = ["a", "ab", "abc", "dddd", "abcd"]
        
        resultado = cadena_mas_larga(lista)
        
        self.assertEqual(resultado, "abcd")
    
    def test_lista_vacia(self):
        resultado = cadena_mas_larga([])
        self.assertEqual(resultado, "")
        

    def test_lista_numero(self):
        lista = ["hyf", "web", 123]
        with self.assertRaises(ValueError):
            cadena_mas_larga(lista)
    
    def test_non_lista (self):
        lista= 1234
        with self.assertRaises(TypeError):
            cadena_mas_larga(lista)
    
    def test_datos_aleatorios(self):

        for _ in range(10):  # probamos múltiples casos dinámicos
            lista = []

            num_valores = random.randint(1, 20)
            for _ in range(num_valores):
                longitud = random.randint(1, 20)
                cadena = ''.join(random.choice(string.ascii_letters) for _ in range(longitud))
                lista.append(cadena)

            resultado = cadena_mas_larga(lista)

            # La cadena devuelta debe ser una de las más largas
            max_len = max(len(c) for c in lista)
            self.assertEqual(len(resultado), max_len)


if __name__ == "__main__":
    unittest.main()