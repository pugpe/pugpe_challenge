"""
Desafio PUG-PE  
ID: 4
Semana: 08/03/2011
Formulado por : Marcel Caraciolo

Problema:
O objetivo deste problema eh transpor uma matriz.


    Seu trabalho eh construir uma funcao transpose que receba uma matriz (em formato de lista de listas) e 
    retorna a matriz transposta desta (em lista de listas).

    Uma matriz transposta eh o resultado da troca de linhas por colunas em uma determinada matriz.

    EX:
       | 1  2 |                      | 1 3 5 |
       | 3  4 |   -> Tranposta ->    | 2 4 6 |
       | 5  6 |

    >>> ret = tranpose([])
    >>> ret
    []
    >>> ret = tranpose([[1]])
    >>> ret
    [1]
    >>> ret = transpose([[1,2]])  
    >>> ret
    [[1],[2]]
    >>> ret = transpose([[1,2], [3,4], [5,6]])
    >>> ret
    [[1,3,5], [2,4,6]]
     
  Seu trabalho eh construir essa funcao.  Favor utilizar Testes usando doctest ou UnitTest para validar sua solucao.

"""



import unittest


class Desafio4(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual([],
                    transpose([]))

    def test_unit_list(self):
        self.assertEqual([1], transpose([[1]]))

    def test_simple_List(self):
        self.assertEqual([[1],[2]], transpose([[1,2]]))

    def test_complex_list(self):    
        self.assertEqual([[1,3,5],[2,4,6]], transpose([[1,2], [3,4], [5,6]]) )


if __name__ == '__main__':
    unittest.main()    
