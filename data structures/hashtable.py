import math

def hashs(key,length):
  return hash(key) % length

# array that indices to linked lists
#   becuase of the linked list we need a node class
# needs to be able to deal with adding and updating values in the hashmap
#   the node has to have some way to determine whether or not to update node or add to the end of the linked list
#       thus the node has to contain the key for the value
#       obviously it needs to contain the value to be able to get the value
# the hashmap should dynammically resize to a new size when the hashmap starts to get full
#   lets say that full = 70% of the indices in the array have a non NULL value
#   resize to double the current array length

class Node():
    def __init__(self, key, value) -> None:
        self.value = value
        self.key = key
        self.next = None

class HashMap():
    def __init__(self) -> None:
        self.table = [None] * 10
        self.length = 10

    def _resize(self) -> None:
        self.length = self.length * 2
        new_table = [None] * (self.length)
        for i in self.table:
            current = i
            while True:
                if current is None:
                    break
                new_table[hashs(current.key, self.length)] = Node(current.key, current.value)
                current = current.next
        self.table = new_table

    def add(self, key, value) -> None:
        hash = hashs(key, self.length)
        if self.table[hash] is None:  # means that there is no collison
            self.table[hash] = Node(key, value)
        else:  # collison, thus check if key already exists in hash and update otherwise add to the end of the linked lsit
            current = self.table[hash]
            while True:
                if current.key == key:  # update the value since key is the same
                    current.value = value
                    break
                if current.next is not None:  # keep going through the linked list
                    current = current.next
                else:
                    current.next = Node(key, value)  # adds the key,value to the linked list
                    break
        if self.table.count(None) <= self.length * 0.3:
            self._resize()

        
    
    def read(self, key) -> None:
        hash = hashs(key, self.length)
        if self.table[hash] is None:  # key not in hashmap
            raise Exception('Key not found in hashmap')
        current = self.table[hash]
        while True:
            if current.key == key:
                return current.value
            if current.next is not None:
                current = current.next
            else:
                raise Exception('Key not found in hashmap')
