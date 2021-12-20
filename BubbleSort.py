from sort import sort
def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-1):
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]


A = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(A)

print ("Sorted array is:")
for i in range(len(A)):
	print ("%d" %A[i]),







