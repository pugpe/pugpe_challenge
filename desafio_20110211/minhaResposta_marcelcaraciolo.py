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

def pack(lista):
    result =[]
    sublista = []
    while lista:
        elemento = lista[0]
        sublista+= [elemento] if elemento in sublista or not sublista else []
        if elemento not in sublista:
            result.append(sublista)
            sublista = [elemento]
        lista = lista[1:]
    if sublista: result.append(sublista)
    return result


        
class Desafio1(unittest.TestCase):

    def test_pack_duplicates(self):
        sampleList = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
        self.assertEqual([['a','a','a','a'],['b'],['c','c'],['a','a'],['d'],['e','e','e','e']],
                    pack(sampleList))

    def test_pack_empty(self):
        sampleList = []
        self.assertEqual([],
                    pack(sampleList))


    def test_pack_simple(self):
        sampleList = ['a','b','c']
        self.assertEqual([['a'],['b'], ['c']],
                    pack(sampleList))




if __name__ == '__main__':
    unittest.main()    
