# contain data at every node
# want to be able to find some data
# want to be able to add data to the start, somewhere in the middle and the end of the linkedlist
# want to be able to delete any node
# want to be able to update data at any node
class Node():
  def __init__(self, value) -> None:
    self.next = None
    self.value = value

class LinkedList():
  def __init__(self) -> None:
    self.head = None
    self.length = 0
  
  def append(self, value) -> None:  # add data to the end of the linked list
    if self.head is None:
      self.head = Node(value)
      self.length += 1
      return
    
    current = self.head
    while True:
      if current.next is None:
        current.next = Node(value)
        self.length += 1
        return
      current = current.next
  
  def to_front(self, value) -> None:  # add data to the front of the linked list
    if self.head is not None:
      old_head = self.head
      self.head = Node(value)
      self.head.next = old_head
      self.length += 1
    else:
      self.append(value)

  def add(self, value, index) -> None:  # add data to linked list at index pos
    if index > self.length - 1:
      raise Exception("index out of bounds")
    
    current = self.head
    for i in range(index - 1):
      current = current.next
    
    
    old_next = current.next
    new = Node(value)
    current.next = new
    new.next = old_next
    self.length += 1

  def del_front(self) -> None:
    if self.head is not None:
      self.head = self.head.next
      self.length -= 1
    else:
      raise Exception("Linked list is empty")
    
  def del_tail(self) -> None:
    if self.head is not None:
      current = self.head
      old = None
      while True:
        if current.next is not None:
          old = current
          current = current.next
        else:
          old.next = None
          self.length -= 1
          return
    
  def del_node(self, index) -> None:
    if index > self.length - 1:
      raise Exception("index out of bounds")
    if self.head is None:
      raise Exception("Linked list is empty")
    current = self.head
    for i in range(index - 1):
      current = current.next
    
    next = current.next
    current.next = next
    # self.length -= 1

  def read(self, index) -> None:
    if index > self.length - 1:
      raise Exception("index out of bounds")
    
    current = self.head
    for i in range(index):
      current = current.next
    
    return current.value
