"""Tree Traversals Notes"""


            10
          /    \
         5     12
        /
       3

2 Types of Tree Traversals:

Depth-First (Stack - recursive) - go down as far as you can down the tree 
                (left or right), then backtrack and go down the next deepest path
Breadth-First (Queue - not recursive) - go down and exhaust by each
                level (check entire first level, check entire second level, etc.)


DEPTH FIRST:
1.) Pre Order DFT (10, 5, 3, 12) - (PRINT), LEFT, RIGHT
2.) In Order DFT (3, 5, 10, 12) - LEFT, (PRINT), RIGHT
3.) Post Order DFT (3, 5, 12, 10) - LEFT, RIGHT, (PRINT)



DEPTH FIRST EXAMPLE:

class BinarySearchTree:
    def __init__(self, value):
        # the value at the current node
        self.value = value
        # reference to this node's left child
        self.left = None
        # reference to this node's right child
        self.right = None

    def insert(self, value):
        # check if the new node's value is less than our current node's value
        if value < self.value:
            # if there's no left child here already, place the new node here
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                # otherwise, repeat the process!
                self.left.insert(value)
        # check if the new node's value is greater than or equal to our 
        # current node's value
        elif value >= self.value:
            # if there's no right child here already, place the new node here
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                # otherwise, repeat the process!
                self.right.insert(value)

    def pre_order_dft(self):`
        if self is None:
            return
        print(self.value)
        self.left.pre_order_dft()
        self.right.pre_order_dft()

    def in_order_dft(self):
        if self is None:
            return
        self.left.pre_order_dft()
        print(self.value)
        self.right.pre_order_dft()

    def post_order_dft(self):
        if self is None:
            return
        self.left.pre_order_dft()
        self.right.pre_order_dft()
        print(self.value)



BREADTH FIRST EXAMPLE:

    def bft_print(self):
        q = []
        q.append(self)

        while len(q) > 0:
            current = q.pop(0)
            print(current.value)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)

    def dft_print(self):
        s = []
        s.append(self)

        while len(q) > 0:
            current = s.pop()
            print(current.value)
            if current.left:
                s.append(current.left)
            if current.right:
                s.append(current.right)