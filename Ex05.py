"""

O QuickSort implementado abaixo utiliza da recursão e do método de dividir e conquistar para ordenar uma coleção de dados. 

Este algoritmo utiliza a recursão para dividir os problemas em fragmentos menores da seguinte forma: explicacao.

A notação Big O desse algoritmo é de O(n log n).

"""

def Ex05():
	def partition(list, low, high):
		pivot = list[high]
		i = low - 1
		for j in range(low, high):
			if list[j] <= pivot:
				i = i + 1
				list[i], list[j] = list[j], list[i]
		list[i + 1], list[high] = list[high], list[i + 1]
		return i + 1
	def quick_sort(list, low, high):
		if low < high:
			pivot = partition(list, low, high)
			quick_sort(list, low, pivot - 1)
			quick_sort(list, pivot + 1, high)
	
	example = [100, -3, 2, 43, 10, 20, 95, 43, 19]
	quick_sort(example, 0, len(example) - 1)
	print(example)

Ex05()