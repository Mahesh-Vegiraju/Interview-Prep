class Node():
  def __init__(self, value) -> None:
    self.right = None
    self.left = None
    self.val = value

class Tree():
  def __init__(self, value) -> None:
    self.root = Node(value)
  
  # insert is a breath wise fashion
  def insert(self, value) -> None:
    queue = []
    queue.append(self.root)
    while len(queue) > 0:
      root = queue.pop(0)
      if root.left is None:
        root.left = Node(value)
        return
      else:
        queue.append(root.left)

      if root.right is None:
        root.right = Node(value)
        return
      else:
        queue.append(root.right)
  
  def is_present(self, value) -> bool:
    queue = []
    queue.append(self.root)
    while len(queue) > 0:
      root = queue.pop(0)
      if root.val == value:
        return True
      
      if root.left is not None:
        queue.append(root.left)
      
      if root.right is not None:
        queue.append(root.right)

  def delete(self, value) -> None:
    stack = []
    stack.append(self.root)
    change_val = None
    to_val = None
    while len(stack) > 0:
      current = stack.pop()
      if current.left is not None:
        stack.append(current.left)
      if current.right is not None:
        stack.append(current.right)

      if current.left is not None and current.left.left is None and current.left.right is None:  # found a leaf node
        to_val = current.left
        current.left = None
        if change_val is not None:
          break
      elif current.right is not None and current.right.left is None and current.right.right is None:
        to_val = current.right
        current.right = None
        if change_val is not None:
          break
      
      if current.val == value:
        change_val = current
    
    change_val.val = to_val.val
    return
      

