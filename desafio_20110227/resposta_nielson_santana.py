"""
Desafio PUG-PE  
ID: 3
Semana: 27/02/2011
Formulado por : Marcel Caraciolo

Problema:
O objetivo deste problema eh converter uma lista de elementos em uma lista de tuplas de 2 elementos.


    Seu trabalho eh construir uma funcao tuplify que receba uma lista como parametro. O retorno dela deve ser esta lista tuplificada.
    
    >>> ret = tuplify([])
    >>> ret
    []
    >>> ret = tuplify([1])
    >>> ret
    None
    >>> ret = tuplify([1,2])
    >>> ret
    [(1,2)]
    >>> ret = tuplify(["x",1,"y",2])
    >>> ret
    [('x',1), ('y',2)]
    >>> ret = tuplify([1,2,3])
    >>> ret
    [(1,2)]

     
  Seu trabalho eh construir essa funcao.  Favor utilizar Testes usando doctest ou UnitTest para validar sua solucao.

"""


#Solucao Pythonica
def tuplify(lista,n=2):
    return zip(*[iter(lista,)]*n) or None


#Solucao criativa
def tuplify1(lista,n=2):
    retorno = []
    for i in xrange(n-1,len(lista),n):
	retorno.append(tuple(lista[i-(n-1):i+1]))
    return retorno or None

import unittest


class Desafio1(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(None,
                    tuplify([]))

    def test_unit_list(self):
        self.assertEqual(None, tuplify([1]))

    def test_simple_List(self):
        self.assertEqual([(1,2)], tuplify([1,2]))

    def test_complex_list(self):    
        self.assertEqual([('x',1),('y',2)], tuplify(['x',1,'y',2]))

    def test_incomplete_list(self):
        self.assertEqual([(1,2)], tuplify([1,2,3]))


class Desafio2(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(None,
                    tuplify1([]))

    def test_unit_list(self):
        self.assertEqual(None, tuplify1([1],3))

    def test_simple_List(self):
        self.assertEqual([(1,2)], tuplify1([1,2]))

    def test_complex_list(self):    
        self.assertEqual([('x',1),('y',2)], tuplify1(['x',1,'y',2]))

    def test_incomplete_list(self):
        self.assertEqual([(1,2)], tuplify1([1,2,3]))

if __name__ == '__main__':
    unittest.main()  
