class Node:
  def __init__(self, value) -> None:
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self) -> None:
    self.head = None
    self.size = 0

  def push(self, value) -> None:
    if self.head is None:
      self.head = Node(value)

    else:
      head = self.head
      for i in range(self.size):
        if head.next is not None:
          head = head.next
      head.next = Node(value)
    self.size += 1
    return
  
  def get_node_at_index(self, index) -> Node:
    if self.head is None:
      raise Exception("LinkedList is empty")
    elif index > self.size - 1:
      raise Exception("Index is out of bounds")
    
    head = self.head
    for i in range(index):
      head = head.next
    return head
  
  def get(self, index):
    return self.get_node_at_index(self, index).value
  
  def find(self, value) -> int:
    if self.head is None:
      return -1
    
    head = self.head
    for i in range(self.size):
      if head is not None and head.value == value:
        return i
      elif head.next is not None:
        head = head.next

    return -1

  
  def modify(self, index, new_value) -> None:
    node = self.get_node_at_index(self, index)
    node.value = new_value
    return
  
  def delete(self, index) -> None:
    if self.head is None:
      raise Exception("LinkedList is empty")
    elif index > self.size - 1:
      raise Exception("Index is out of bounds")
    
    head = self.head
    prev = None
    for i in range(index):
      prev = head
      head = head.next
    
    if i == self.size:
      prev.next = None
      head = None
    elif i < self.size:
      prev.next = head.next
      head = None
      
    return
