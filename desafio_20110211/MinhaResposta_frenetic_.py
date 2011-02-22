# -*- coding: utf-8 -*-
"""
Desafio PUG-PE  
ID: 1
Semana: 11/02/2011

Problema:

    Dado uma lista de elementos, o objetivo eh converter esta lista em uma lista de sub-listas de elementos consecutivos duplicados.
    Assim que um elemento subsequente for diferente do anterior, a sublista eh gerada e passa para o proximo elemento. Entao 
    no exemplo abaixo dado 5 a's quando encontrar um b ele gera a sublista de 5 a's e comeca a gerar a sublista de b's ate encontrar um
    elemento que nao seja b, e assim sucessivamente. 
    >>> x = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
    >>> ret = pack(x)
    >>> ret
    >>> [['a','a','a','a'],['b'],['c','c'],['a','a'],['d'],['e','e','e','e']]
    >>> x = ['a', 'b', 'c']
    >>> ret = pack(x)
    >>> ret 
    >>>[['a'], ['b'], ['c']]
    >>> x = []
    >>> ret = pack(x)
    >>> ret
    >>> []
     
  Seu trabalho eh construir essa lista de elementos.  Favor utilizar Testes usando doctest ou UnitTest para validar sua solucao.

"""

import unittest


class Desafio1(unittest.TestCase):

    def test_pack_duplicates(self):
        sampleList = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
        self.assertEqual([['a','a','a','a'],['b'],['c','c'],['a','a'],['d'],['e','e','e','e']], self.solucaoN00b(sampleList))
        self.assertEqual([['a','a','a','a'],['b'],['c','c'],['a','a'],['d'],['e','e','e','e']], self.solucaoLammer(sampleList))

    def test_pack_empty(self):
        sampleList = []
        self.assertEqual([], self.solucaoN00b(sampleList))
        self.assertEqual([], self.solucaoLammer(sampleList))

    def test_pack_one(self):
        sampleList = ['a']
        self.assertEqual([['a']], self.solucaoN00b(sampleList))
        self.assertEqual([['a']], self.solucaoLammer(sampleList))

    def test_pack_two(self):
        sampleList = ['a', 'b']
        self.assertEqual([['a'], ['b']], self.solucaoN00b(sampleList))
        self.assertEqual([['a'], ['b']], self.solucaoLammer(sampleList))




    def solucaoN00b(self, lista):
        """Resolvendo da maneira mais simples possível"""
        if lista == []:
            return []
        
        numero_de_itens = len(lista)
        i = 0
        resultado = []
        lista_auxiliar = []

        elemento_da_iteracao = lista[i]
        lista_auxiliar.append(elemento_da_iteracao)
        i = i + 1

        while i < numero_de_itens:
            if (lista[i] == elemento_da_iteracao):
                lista_auxiliar.append(elemento_da_iteracao)
            else:
                resultado.append(lista_auxiliar)
                elemento_da_iteracao = lista[i]
                lista_auxiliar = []
                lista_auxiliar.append(elemento_da_iteracao)

            i = i + 1

        resultado.append(lista_auxiliar)
        return resultado


    def solucaoLammer(self, lista):
        """Utilizando a lista como se fosse uma pilha"""
        if lista == []:
            return []
        
        resultado = []
        lista.reverse()

        temp = [lista.pop()]

        while lista:
            i = lista.pop()
            if (i in temp):
                temp.append(i)
            else:
                resultado.append(temp)
                temp = [i]

        resultado.append(temp)
        
                
        return resultado
                    


if __name__ == '__main__':
    unittest.main()
