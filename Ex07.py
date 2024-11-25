"""

A diferença entre o desempenho de uma busca linear e o QuickSelect é que . O QuickSelect tende a ser mais eficiente.

"""

def Ex07():
	def quick_select(array, low, high, k):
    		if low == high:
        		return array[low]

    		pivot_index = partition(array, low, high)

    		if k == pivot_index:
        		return array[k]
    		elif k < pivot_index:
        		return quick_select(array, low, pivot_index - 1, k)
    		else:
        		return quick_select(array, pivot_index + 1, high, k)


	def partition(array, low, high):
    		pivot = array[high]
    		i = low - 1

    		for j in range(low, high):
        		if array[j] <= pivot:
            			i += 1
            			array[i], array[j] = array[j], array[i]

    		array[i + 1], array[high] = array[high], array[i + 1]

    		return i + 1

	array = [4324, 123, 9, 12, 5, 4, 6, 2, 1, 9, 93, 233, 132]
	k = 3
	result = quick_select(array, 0, len(array) - 1, k - 1)
	print(result)

Ex07()