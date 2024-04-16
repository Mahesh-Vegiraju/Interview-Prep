import sys
import math
sys.path.insert(0, '/Users/maheshvegiraju/Documents/Personal/Projects/Interview-Prep/data structures/')

from linkedlist import LinkedList

list = LinkedList()

# testing adding value and reading
list.append(5)
assert list.read(0) == 5

list.append(3)
assert list.read(1) == 3
assert list.read(0) == 5

print('passed add and read')

list.to_front(6)
assert list.read(0) == 6
print('passed adding to head')

list.add(9, 1)
assert list.read(1) == 9
print('passed adding inbetween')

list.del_front()
assert list.read(0) == 9
print('passed del front')

list.del_tail()
assert list.read(1) == 5
print('passed del tail')

list.append(9)
list.del_node(1)
print(list.read(0))
print(list.read(1))
print(list.read(2))
print(list.length)
assert list.read(0) == list.read(1)
print('passed del middle')