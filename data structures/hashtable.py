import math

def _hash(key, size):
    return hash(key) % size

class LinkedListNode:
    def __init__(self, key, data):
        self.data = data
        self.key = key
        self.next = None

    def print(self):
        if self.key:
            head = self
            while True:
                print(f"[{head.key}, {head.data}]", end='')
                if head.next is not None:
                    print(" --> ", end='')
                    head = head.next
                else:
                    print()
                    return

        
class HashTable:
    def __init__(self):
        self.table = [None] * 10
        
    def rehash(self, new_table):
        size = len(new_table)
        for linked_list in self.table:
            if linked_list is not None:
                head = linked_list
                while True:
                    new_table[_hash(head.key, size)] = head
                    if head.next is not None:
                        head = head.next
                    else:
                        break
        
        self.table = new_table
        return
    
    def resize(self):
        null_count = self.table.count(None)
        if len(self.table) - null_count == math.floor(len(self.table)*0.8):
            new_table = [None] * (2 * len(self.table))
            self.rehash(new_table)
        return
    
    def insert(self, key, data):
        hashed = _hash(key, len(self.table))
        if self.table[hashed] is not None:
            head = self.table[hashed]
            while True:
                if head.next is not None and head.key != key:
                    head = head.next
                elif head.key == key:
                    head.data = data
                    break
                else:
                    head.next = LinkedListNode(key, data)
                    break
        else:
            self.table[hashed] = LinkedListNode(key, data)
            
        self.resize()
        return
            
    def read(self, key):
        hashed = _hash(key, len(self.table))
        if self.table[hashed] is None:
            raise Exception("key not found")
        else:
            head = self.table[hashed]
            while True:
                if head.next is not None and head.key != key:
                    head = head.next
                elif head.key == key:
                    return head.data
                else:
                    raise Exception("key not found")
        return

    def print(self):
        for i in range(len(self.table)):
            print(f'index [{i}]: ', end='')
            if self.table[i] is not None:
                self.table[i].print()
            else:
                print()
