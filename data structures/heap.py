class Heap():
  def max_heapify(self, i):
    largest = i

    if i*2 + 1 < len(self.arr) and self.arr[i*2 + 1] > self.arr[largest]:
      largest = i * 2 + 1
    if i*2 + 2 < len(self.arr) and self.arr[i*2 + 2] > self.arr[largest]:
      largest = i * 2 + 2
    
    if largest != i:
      arr[largest], arr[i] = arr[i], arr[largest]
      self.max_heapify(largest)

  def _build_heap(self):
    for i in range(len(self.arr) // 2 - 1, -1, -1):
      self.max_heapify(i)

  def __init__(self, arr) -> None:
    self.arr = arr
    self._build_heap()

arr = [4, 7, 2, 1, 9, 5, 8, 3, 6, 10]
heap = Heap(arr)
print(heap.arr)