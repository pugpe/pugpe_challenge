"""
Desafio PUG-PE  
ID: 5
Semana: 16/03/2011
Formulado por : Rafael Brandao

Problema:
	Voce decidiu organizar uma festa na sua casa e fez diversas tortas para celebrar. Entretanto,
	para nao causar discordia entre as pessoas na festa, voce decide cortar as tortas em pedacos
	de mesmo tamanho para distribuir. Voce nao deve servir mais de um pedaco para cada pessoa, e voce
	tambem quer receber um pedaco. O desafio eh descobrir qual eh o tamanho do maior pedaco que todos
	podem receber. Vale ressaltar que nao tem problema se voce decidir jogar algum resto de torta fora,
	o importante eh nao causar discordia em sua festa. :)

	Cada torta pode ser vista como um cilindro de altura 1. Voce recebera uma lista contendo o raio de
	cada torta que voce tem disponivel e um inteiro com o numero de amigos que voce convidou para a festa.
	Retorne o valor do maior pedaco que cada um pode receber.

	Restricoes:
		numero de tortas, numero de amigos, raio >= 1
		numero de tortas, numero de amigos, raio <= 10000

	>>> solve( [4,3,3], 3 )
	25.132741228718345
	>>> solve( [5], 24 )
	3.1415926535897931
	>>> solve( [1,4,2,3,4,5,6,5,4,2], 5 )
	50.26548245743669


	Sua resposta pode ter um erro absoluto de ate 10^-3.

"""

import unittest

class Desafio5(unittest.TestCase):
	EPS = 1e-3
	def test_first_party(self):
		self.assertTrue( abs( solve( [4,3,3], 3 ) - 25.132741228718345 ) <= self.EPS )
	def test_lonely_pie(self):
		self.assertTrue( abs( solve( [5], 24 ) - 3.1415926535897931 ) <= self.EPS )
	def test_great_party(self):
		self.assertTrue( abs( solve( [1,4,2,3,4,5,6,5,4,2], 5 ) - 50.26548245743669 ) <= self.EPS )


if __name__ == '__main__':
	unittest.main()
