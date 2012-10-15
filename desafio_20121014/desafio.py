"""
Desafio PUG-PE
ID: 7
SEMANA: 15/10/2012

Problema: Achar o conjunto de todas as partições de um dado conjunto de strings.
    Ex:
    >>> x = ['a', 'b']
    >>> ret = subset(x)
    >>> ret
    >>> ['', a', 'b', ('a', 'b')]
    >>> y = ['a', 'b', 'c']
    >>> ret = subset()
    >>> ret
    >>> ['', 'a', 'b', 'c', ('a', 'b'), ('a', 'c'), ('b', 'c'), ('a', 'b', 'c')]

    Favor utilizar Testes usando doctest ou UnitTest para validar sua solucao.
"""

import unittest


class Desafio7(unittest.TestCase):

    def test_find_powerset(self):
        set_1 = ['a', 'b']
        set_2 = ['a', 'b', 'c']
        set_3 = ['']
        set_4 = ['a']
        set_5 = []
        self.assertEqual(set([('',), ('a',), ('b',), ('a', 'b')]), subset(set_1))
        self.assertEqual(set([('',),('a',), 'b', 'c', ('a', 'b'), ('a', 'c'), ('b', 'c'), ('a', 'b', 'c')]), subset(set_2))
        self.assertEqual(set([('',)]), subset(set_3))
        self.assertEqual(set([('',),('a',)]), subset(set_4))
        self.assertEqual(set([]), subset(set_5))

