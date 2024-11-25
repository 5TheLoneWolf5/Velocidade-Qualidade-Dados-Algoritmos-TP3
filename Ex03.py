""" 

Este algoritmo funciona da seguinte forma:

A função recebe quatro argumentos: primeiro o número de discos a serem movidos, o disco de origem, o destino do disco e a haste de auxílio para movimentar os discos.

Para cada chamada, a função se chamará duas vezes, recursivamente. Seguindo o princípio da pilha de chamadas, a última chamada que chegar no caso base será a primeira a ser resolvida e retornada.

A primeira chamada move o disco de origem para a haste auxiliar.
A segunda retorna os discos movidos para a haste auxilar para a haste de destino.

Recursivamente, a função se chama até chegar no caso base (0 discos a serem movidos). Com isso, as funções são retornadas, e entre elas, é printado as ações de movimentação dos discos até concluir o objetivo da Torre de Hanói.

Este algoritmo realiza com sucesso seu objetivo de movimentar os discos para uma nova haste, seguindo as regras do jogo.

A complexidade temporal desse algoritmo é de O(2^n) (exponencial).

"""

import os

def Ex03(n, from_rod, to_rod, aux_rod):
	if n == 0:
		return
	Ex03(n-1, from_rod, aux_rod, to_rod)
	print("Disco", n, "movido da haste", from_rod, "para a haste", to_rod)
	Ex03(n-1, aux_rod, to_rod, from_rod)

Ex03(3, 'A', 'C', 'B')