class Node():
  def __init__(self, value) -> None:
    self.left = None
    self.right = None
    self.val = value

class Tree():
  def __init__(self, value) -> None:
    self.root = value

  def insert(self, value) -> None:
    current = self.root
    while True:
      if value < current.val and current.left is not None:
        current = current.left
      elif value < current.val and current.left is None:
        current.left = Node(value)
        return
      
      if value > current.val and current.right is not None:
        current = current.right
      elif value > current.val and current.right is None:
        current.right = Node(value)
        return
      
  def find(self, value) -> bool:
    current = self.root
    while True:
      if current.val == value:
        return True

      if value < current.val and current.left is not None:
        current = current.left
      elif value < current.val and current.left is None:
        return False
      
      if value > current.val and current.right is not None:
        current = current.right
      elif value > current.val and current.right is None:
        return False

  # 3 different cases
  # the node is a leaf node
  # the node has one child node
  # the node has two child nodes

  # leaf node
  # we can just set the corresponding pointer in the parent node = None

  # the node has one child node
  # we can set the nodes val to the child nodes val
  # we can set the nodes corresponding pointer to the child nodes corresponding pointer
  # we can set the parent nodes corresponding pointer to the child node
      
  # the node has two child nodes
  # find the next highest val node (this means we are going to walk down the right childs subtree on the left side)
  # replace the node with the next highest val node
  def delete(self, value) -> None:
    current = self.root
    while True:
      if value < current.val and current.left is not None and current.left.val == value:
        if current.left.left is None and current.left.right is None:  # leaf node
          current.left = None
        elif current.left.left is not None and current.left.right is None:  # one child node on the left
          current.left.val = current.left.left.val
          current.left = current.left.left
        elif current.left.left is None and current.left.right is not None:
          current.left.val = current.left.right.val
          current.right = current.left.right
        else:  # two children
          walk = current.left.right
          while True:
            if walk.left is not None and walk.left.left is None:
              break
            else:
              walk = walk.left
          # change the value
          # change the parent pointer
          # change walk parent pointer
          current.left.val = walk.left.val
          if walk.left.left is not None:
            walk.left = walk


      elif value < current.val and current.right is not None and current.right.val == value:
        if current.right.left is None and current.right.right is None:
          current.right = None
        elif current.right.left is not None and current.right.right is None:
          current.right.val = current.right.left.val
          current.right = current.right.left
        elif current.right.right is not None and current.right.left is None:
          current.right.val = current.right.right.val
          current.right = current.right.right