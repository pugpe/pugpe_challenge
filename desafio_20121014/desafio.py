#-*- coding:utf-8 -*-

"""
Desafio PUG-PE
ID: 7
SEMANA: 15/10/2012

Problema: Achar todas as partições de uma dada lista de strings.
    Ex:
    >>> x = {'a', 'b'}
    >>> powerset(x)
    {frozenset({''}), frozenset({'a'}), frozenset({'b'}), frozenset({'a', 'b'})}
    >>> y = {'a', 'b', 'c'}
    >>> ret = powerset(y)
    {frozenset({''}), frozenset({'a'}), frozenset({'b'}), frozenset({'c'}), frozenset({'a', 'b'}), frozenset({'a', 'c'}), frozenset({'b', 'c'}), frozenset({'a', 'b', 'c'})}

    Favor utilizar Testes usando doctest ou UnitTest para validar sua solucao.
"""

import unittest
import itertools

def iterpowerset(s):
    l = list(s)
    for n in range(len(l)+1):
        for c in itertools.combinations(l, n):
            yield c

def powerset(set):
    return {frozenset(s) for s in iterpowerset(set)}


class Desafio7(unittest.TestCase):

    def test_find_powerset(self):
        set_1 = {'a', 'b'}
        set_2 = {'a', 'b', 'c'}
        set_3 = {''}
        set_4 = {'a'}
        set_5 = {}
        self.assertEqual({
            frozenset({}),
            frozenset({'a'}), frozenset({'b'}),
            frozenset({'a', 'b'})
            }, powerset(set_1))
        self.assertEqual({
            frozenset({}),
            frozenset({'a'}), frozenset({'b'}), frozenset({'c'}),
            frozenset({'a', 'b'}), frozenset({'a', 'c'}), frozenset({'b', 'c'}),
            frozenset({'a', 'b', 'c'})
            }, powerset(set_2))
        self.assertEqual({
            frozenset({}),
            frozenset({''}),
            }, powerset(set_3))
        self.assertEqual({
            frozenset({}),
            frozenset({'a'})
            }, powerset(set_4))
        self.assertEqual({frozenset({})}, powerset(set_5))

if __name__ == '__main__':
    unittest.main()
