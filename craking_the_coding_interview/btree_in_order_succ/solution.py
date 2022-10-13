class TreeNode:
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def in_order_succ(node: TreeNode) -> TreeNode:
    if node != None:
        if node.right:
          tmp = node.right

          while tmp.left:
            tmp = tmp.left

          return tmp

        else:
            if node.parent:
                if node.parent.value < node.value:
                    tmp = node.parent
                    while tmp and tmp.value < node.value:
                        tmp = tmp.parent
                    return tmp
                return node.parent

    return None
