"""Give a sorted array, create a binary search tree and print out the 
   tree in inorder, preorder and postorder
"""
# Create a node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# method for creating binary search tree from sorted array
def sorted_array_to_bst(nums):
    # Your code goes here
    pass

def inorder(node):
    # Your code goes here
    pass

def preorder(node):
    # Your code goest here
    pass

def postorder(node):
    # Your code goes here
    pass


#--- EXERCISE ---#
array = [2,4,5,7,8,9,10,14,23,46]
bst = sorted_array_to_bst(array)

# print out your result
inorder(bst) #2 -> 4 -> 5 -> 7 -> 8 -> 9 -> 10 -> 14 -> 23 -> 46 ->

preorder(bst) #9 -> 2 -> 4 -> 5 -> 7 -> 8 -> 10 -> 14 -> 23 -> 46 ->

postorder(bst) #2 -> 4 -> 5 -> 7 -> 8 -> 10 -> 14 -> 23 -> 46 -> 9 ->
