"""
Desafio PUG-PE  
ID: 2
Semana: 19/02/2011

Problema:

    Escreva uma funcao que reverta a ordem das palavras em uma string. Por exemplo, sua funcao deve transformar a string 'Do or do not,
    there is no try.'  para 'try. no is there not, or Do'.  Assuma que todas palavras sao separadas por espaco e trate todos os sinais de pontuacao
    como caracteres.

    >>> x =  "attempt"
    >>> ret = reverse_string(x)
    >>> ret
    attempt
    >>> x = 'I am going to jail.'
    >>> ret = reverse_string(x)
    jail. to going am I
    >>> x = 'Python como linguagem eh poderosa, facil e divertida.'
    >>> x = []
    >>> ret = reverse_string(x)
    >>> ret
    divertida. e facil poderosa, eh linguagem como Python
     
  Seu trabalho eh construir essa lista de elementos.  Favor utilizar Testes usando doctest ou UnitTest para validar sua solucao.

"""

import unittest


class Desafio1(unittest.TestCase):

    def test_simple_string(self):
        sampleString = 'attempt'
        self.assertEqual('attempt',
                    reverse_string(sampleString))

    def test_empty_string(self):
        sampleString = ''
        self.assertEqual('',
                    reverse_string(sampleString))

    def test_complex_string(self):
        sampleString = 'Python como linguagem eh poderosa, facil e divertida.'
        self.assertEqual('divertida. e facil poderosa, eh linguagem como Python',
                    reverse_string(sampleString))


if __name__ == '__main__':
    unittest.main()    
