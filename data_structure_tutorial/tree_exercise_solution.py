
# Create a node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# method for creating binary search tree from sorted array
def sorted_array_to_bst(nums):
    if not nums:
        return None
    mid_num = len(nums)//2
    node = Node(nums[mid_num])
    node.left = sorted_array_to_bst(nums[:mid_num])
    node.right = sorted_array_to_bst(nums[mid_num+1:])
    return node

def inorder(node):
    if node:
        # Traverse left
        inorder(node.left)
        # Traverse root
        print(str(node.value) + " -> ", end='')
        # Traverse right
        inorder(node.right)

def preorder(node):
    if node:
        # Traverse left
        print(str(node.value) + " -> ", end='')
        # Traverse root
        inorder(node.left)
        # Traverse right
        inorder(node.right)

def postorder(node):
    if node:
        # Traverse left
        inorder(node.left)
        # Traverse root
        inorder(node.right)
        # Traverse right
        print(str(node.value) + " -> ", end='')

#--- EXERCISE ---#
array = [2,4,5,7,8,9,10,14,23,46]
bst = sorted_array_to_bst(array)

# print out your result
print("\nInorder traversal ")
inorder(bst)

print("\n\nPreorder traversal ")
preorder(bst)

print("\n\nPostorder traversal ")
postorder(bst)
