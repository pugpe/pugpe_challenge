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
        self.assertEqual([['a','a','a','a'],['b'],['c','c'],['a','a'],['d'],['e','e','e','e']],
                    pack(sampleList))

#resposta lucrodsilva
def pack(sampleList):
    result = []
    
    for i in sampleList:
        if (not result) or (i not in result[-1]):
            result.append([i])
            continue
        result[-1].append(i)
    
    return result

if __name__ == '__main__':
    unittest.main()    
