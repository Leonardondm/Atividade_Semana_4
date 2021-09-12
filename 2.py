#ShellSort

arr2 = [12, 34, 54, 2, 3, 5, 66, 10, 2, 55]

def shellSort(arr):
	gap = len(arr) // 2 # Inicializa o intervalo

	while gap > 0:
		i = 0
		j = gap
		
		# Verifica o array da esquerda para direita
		# até o último índice possível de j
		while j < len(arr):
	
			if arr[i] >arr[j]:
				arr[i],arr[j] = arr[j],arr[i]
			
			i += 1
			j += 1
		
			# agora olha do indice i atual para a esquerda
			# e troca os valores que nao estao na ordem
			k = i
			while k - gap > -1:

				if arr[k - gap] > arr[k]:
					arr[k-gap],arr[k] = arr[k],arr[k-gap]
				k -= 1

		gap //= 2


# teste
shellSort(arr2)
print("Array ordenado",arr2)