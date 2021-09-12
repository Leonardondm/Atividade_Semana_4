#Counting sort

# Funcao que ordena o array dado arr[]
def count_sort(arr):
	max_element = int(max(arr))
	min_element = int(min(arr))
	range_of_elements = max_element - min_element + 1
	# Cria um array count para armazenar a conta de  
	# elementos individuais e inicializa com 0
	count_arr = [0 for _ in range(range_of_elements)]
	output_arr = [0 for _ in range(len(arr))]

	# armazena cada caracter
	for i in range(0, len(arr)):
		count_arr[arr[i]-min_element] += 1

	# Altera count_arr[i] para que count_arr[i] contenha a
	# posicao atual deste elemento  no array de saida
	for i in range(1, len(count_arr)):
		count_arr[i] += count_arr[i-1]

	# constriu o array de saida
	for i in range(len(arr)-1, -1, -1):
		output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
		count_arr[arr[i] - min_element] -= 1

	# Copia o array de saida para arr, para que arr 
	# tenha os caracteres ordenados
	for i in range(0, len(arr)):
		arr[i] = output_arr[i]

	return arr


# Teste
arr = [22,-5, -10, 0, -3, 8, 5, -1, 10, 55]
ans = count_sort(arr)
print("Array ordenado " + str(ans))
