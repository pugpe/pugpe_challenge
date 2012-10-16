"""
Desafio PUG-PE
ID: 7
SEMANA: 15/10/2012

Problema: Achar todas as partições de uma dada lista de strings.
    Ex:
    >>> x = ['a', 'b']
    >>> ret = partitions(x)
    >>> ret
    >>> [[''], ['a'], ['b'], ['a', 'b']]
    >>> y = ['a', 'b', 'c']
    >>> ret = partitions()
    >>> ret
    >>> [[''], ['a'], ['b'], ['c'], ['a', 'b'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']]

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
        self.assertEqual([[''], ['a'], ['b'], ['a', 'b']], subset(set_1))
        self.assertEqual([[''], ['a'], ['b'], ['c'], ['a', 'b'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']], subset(set_2))
        self.assertEqual([''], subset(set_3))
        self.assertEqual(['', ['a']], subset(set_4))
        self.assertEqual([], subset(set_5))

