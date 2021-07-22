"""
You are given the values from a preorder and an inorder tree traversal. Write a
function that can take those inputs and output a binary tree.

*Note: assume that there will not be any duplicates in the tree.*

Example:
Inputs:
preorder = [5,7,22,13,9]
inorder = [7,5,13,22,9]

Output:
    5
   / \
  7  22
    /  \
   13   9
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder, inorder):
    # Your code here
    def helper(in_left = 0, in_right = len(inorder)):
        nonlocal pre_idx
        if in_left == in_right:
            return None
        
        root_val = preorder[pre_idx]
        root = TreeNode(root_val)

        idx = idx_map[root_val]

        pre_idx += 1
        root.left = helper(in_left, idx)
        root.right = helper(idx + 1, in_right)
        return root
        
    pre_idx = 0
    idx_map = {}
    for idx, val in enumerate(inorder):
        idx_map[val] = idx
    return helper()


# test
preorder = [5,7,22,13,9]
inorder = [7,5,13,22,9]

t = build_tree(preorder, inorder)
print(t.right.right.val)

