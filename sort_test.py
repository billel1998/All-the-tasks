from sort import sort
from random import randint

sort1 = sort()
def InsertionSort(arr):

	for i in range(1, len(arr)):

		key = arr[i]
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key

def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-1):
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]

def test_bubble_sort():


    size = randint(90, 100)
    A = []
    for i in range(0, size):
        A.append(randint(90, 100))
    A = sort1.bubbleSort(A)

    status = True
    for i in range(0, len(A) - 1):
        if A[i] > A[i + 1]:
            status = False
    assert status, " Your method is not working  "



def test_Insertion_sort():


    size = randint(90, 100)
    A = []
    for i in range(0, size):
        A.append(randint(90, 100))
    A = sort1.InsertionSort(A)

    status = True
    for i in range(0, len(A) - 1):
        if A[i] > A[i + 1]:
            status = False
    assert status, " Your method is not working "
