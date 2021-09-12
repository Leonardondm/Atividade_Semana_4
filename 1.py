#SelectionSort
import sys
A = [64, 25, 12, 22, 11]

# Percorre todos os elementos do array
for i in range(len(A)):
	
	# Encontra o menor elemento no array
	min_idx = i
	for j in range(i+1, len(A)):
		if A[min_idx] > A[j]:
			min_idx = j
			
	# troca o menor elemento encontrado
	A[i], A[min_idx] = A[min_idx], A[i]

#Teste
print ("array ordenado")
for i in range(len(A)):
	print("%d" %A[i]),
