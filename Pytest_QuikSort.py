def partition(array, low, high):

  pivot = array[high]
  i = low - 1

  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])

  (array[i + 1], array[high]) = (array[high], array[i + 1])

  return i + 1

def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)

    quickSort(array, low, pi - 1)

    quickSort(array, pi + 1, high)

def test_Quick():
    """ Algorithm of   quick sort  """
    size = randint(10, 10)
    A = []
    for i in range(0, size):
      A.append(randint(0, 100))
    print(A)
    high = size - 1
    B = quickSort(A, 0, high)
    print(B)
    status = True
    for i in range(0, high):
      if B[i] > B[i + 1]:
        status = False
    assert status, " your method is not working well  "
a = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(a)

size = len(a)

quickSort(a, 0, size - 1)

print('Sorted Array ')
print(a)