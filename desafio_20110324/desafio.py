"""
Desafio PUG-PE  
ID: 6
Semana: 25/03/2011
Formulado por : Rafael Brandao

Problema:
	Alice e Bob estavam entediados e decidiram jogar um jogo bem simples
	para passar o tempo. As regras do jogo sao:
	* um jogador escolhe uma string
	* para cada letra da string, se a letra fizer parte do nome do jogador,
	  o jogador adiciona 1 na pontuacao daquela frase
	* a letra faz parte do nome do jogador se houver ela em maiuscula ou
	  em minuscula na string, ou seja, nao eh case sensitive
	* o jogador que fizer a maior pontuacao naquela string eh o vencedor
	
	Por exemplo, a string "aalbicee" daria a Alice uma pontuacao de 7, enquanto
	Bob so ganharia um ponto.
	
	Implemente uma funcao chamada solve que recebe uma string e determina quem
	ganharia mais pontos. Retorne a string "Alice" se for Alice, "Bob" se for Bob,
	ou "Empate" se houver um empate.
	

	Restricoes:
		0 < tamanho da string < 100000

	>>> solve( "aalbicee" )
	"Alice"
	>>> solve( "bBbal" )
	"Bob"
	>>> solve( "balbicebob" )
	"Empate"

"""

import unittest

class Desafio6(unittest.TestCase):
	def test_alice_wins(self):
		self.assertEqual( solve( "aalbicee" ), "Alice" )
	def test_bob_wins(self):
		self.assertEqual( solve( "bBbal" ), "Bob" )
	def test_draw(self):
		self.assertEqual( solve( "balbicebob" ), "Empate" )


if __name__ == '__main__':
	unittest.main()
