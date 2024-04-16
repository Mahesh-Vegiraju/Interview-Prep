import sys
import math
sys.path.insert(0, '/Users/maheshvegiraju/Documents/Personal/Projects/Interview-Prep/data structures/')

from hashtable import HashMap

table = HashMap()

# test adding to table and then reading
table.add('a', 1)
assert table.read('a') == 1
print('passed adding and reading')
# table = HashMap()

# test if error is thrown when key not in table
try:
  table.read('b')
except:
  print('passed throwing exception when reading key that is not in table')

# test update
  table.add('a', 2)
  assert table.read('a') == 2
  print('passed updating value')

# test resizing
table = HashMap()
i = 0
while table.length == 10:
  table.add(i, 0)
  i += 1
print('passed resizing in ' + str(i))
