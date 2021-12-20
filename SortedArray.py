
import sys

A = [64, 25, 12, 22, 11]
for i in range(len(A)):
    min = i
    k = i+1
    for j in range(k, len(A)):
        if A[min] > A[j]:
            min = j
    A[i], A[min] = A[min], A[i]


print("Sorted array")
print(A)



