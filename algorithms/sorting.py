# merge sort
def merge(arr1, arr2):
  new = []
  i, j = 0, 0
  if len(arr1) > 0 and len(arr2) > 0:
    while len(new) != len(arr1) + len(arr2):
      if i < len(arr1) and j < len(arr2) and arr1[i] <= arr2[j]:
        new.append(arr1[i])
        i += 1
      elif i < len(arr1) and j < len(arr2) and arr2[j] <= arr1[i]:
        new.append(arr2[j])
        j += 1
      elif i < len(arr1):
        new += arr1[i:]
      elif j < len(arr2):
        new += arr2[j:]
  elif len(arr1) > 0:
    return arr1
  else:
    return arr2
  return new

def merge_sort_helper(arr):
  if len(arr) > 1:
    low, high = 0, len(arr) - 1
    middle = (high - low) // 2
    arr1 = merge_sort_helper(arr[low:middle + 1])
    arr2 = merge_sort_helper(arr[middle + 1:high + 1])
    return merge(arr1, arr2)
  else:
    return arr

def merge_sort(arr):
  return merge_sort_helper(arr)

def count_sort(arr, place):
  digits = [0 for i in range(10)]
  new_arr = [0 for i in range(len(arr))]
  for i in arr:
    digits[i // 10**place % 10] += 1

  for i in range(1, len(digits)):
    digits[i] += digits[i - 1]
  
  for i in range(len(digits) - 1, 0, -1):
    digits[i] = digits[i - 1]
  digits[0] = 0

  for i in arr:
    place_i = i // 10**place % 10
    new_arr[digits[place_i]] = i
    digits[place_i] += 1
  
  return new_arr
  # iterate through arr and for each seen digit, put into list at digits[digit] then do digits[digit] += 1

# radix sort
def radix_sort(arr):
  place = 0
  amount = 1
  _max = max(arr)
  while amount < _max:
    arr = count_sort(arr, place)
    amount *= 10
    place += 1
  return arr


# quick sort
def partition(arr, i, j):
  pivot =  arr[i]
  low, high = i, j
  while low < high:
    while low < j and arr[low] <= pivot:
      low += 1 
    while high > i and arr[high] >= pivot:
      high -= 1
    if high > low:
      arr[low], arr[high] = arr[high], arr[low]
  arr[i], arr[high] = arr[high], arr[i]
  return high

def quick_sort_helper(arr, low, high):
  if low < high:
    j = partition(arr, low, high)
    quick_sort_helper(arr, low, j)
    quick_sort_helper(arr, j + 1, high)

def quick_sort(arr):
  quick_sort_helper(arr, 0, len(arr) - 1)
  
# bubble sort
def bubble_sort(l):
  for i in range(len(l)):
    for j in range(len(l) - i - 1):
      if l[j + 1] < l[j]:
        temp = l[j]
        l[j] = l[j + 1]
        l[j + 1] = temp

# insertion sort
def insertion_sort(l):
  for i in range(1, len(l)):
    check = l[i]

    j = i - 1
    while j >= 0 and l[j] > check:
      l[j + 1] = l[j]
      j -= 1
    l[j + 1] = check

# heap sort
class Heap():
  def max_heapify(self, i):
    largest = i

    if i*2 + 1 < self.size and self.arr[i*2 + 1] > self.arr[largest]:
      largest = i * 2 + 1
    if i*2 + 2 < self.size and self.arr[i*2 + 2] > self.arr[largest]:
      largest = i * 2 + 2
    
    if largest != i:
      arr[largest], arr[i] = arr[i], arr[largest]
      self.max_heapify(largest)

  def _build_heap(self):
    for i in range(len(self.arr) // 2 - 1, -1, -1):
      self.max_heapify(i)

  def __init__(self, arr) -> None:
    self.arr = arr
    self.size = len(arr)
    self._build_heap()

def heap_sort(arr):
  heap = Heap(arr)
  sorted = []
  while heap.size > 0:
    heap.arr[0], heap.arr[heap.size - 1] = heap.arr[heap.size - 1], heap.arr[0]
    sorted.append(heap.arr[heap.size - 1])
    heap.size -= 1
    heap.max_heapify(0)
  return sorted

# selection sort
def selection_sort(arr):
  for i in range(len(arr)):
    min_index = i
    for j in range(i, len(arr)):
      if arr[j] < arr[min_index]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
        
arr = [1, 5, 9, 0, -1, 2]
bubble_sort(arr)
print(arr)
arr = [1, 5, 9, 0, -1, 2]
insertion_sort(arr)
print(arr)
arr = [1, 5, 9, 0, -1, 2]
quick_sort(arr)
print(arr)
arr = [1, 5, 9, 0, -1, 2]
arr = merge_sort(arr)
print(arr)
arr = [1, 5, 9, 0, -1, 2]
selection_sort(arr)
print(arr)
arr = [1, 5, 9, 0, 15, 2]
arr = radix_sort(arr)
print(arr)
arr = [1, 5, 9, 0, -1, 2]
arr = heap_sort(arr)
print(arr)