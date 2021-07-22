"""
You are given a binary tree.

Write a function that can return the inorder traversal of node values.

Example:
Input:

   3
    \
     1
    /
   5

Output: [3,5,1]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    # Your code here
    # o an in order dft
    s = []
    result = []
    while True:
      while root:
        s.append(root)
        root = root.left
      if len(s) == 0:
        return result
      node = s.pop()
      result.append(node.val)
      
      root = node.right

n = TreeNode(3)
n.right = TreeNode(1)
n.right.left = TreeNode(5)

res = inorder_traversal(n)
print(res)
