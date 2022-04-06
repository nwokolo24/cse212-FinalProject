# Tree traversal in Python

# Node Class implementation
class Node:
    """
    Each node contains an item and a pointer to a left and right node
    """
    def __init__(self, item):
        """
        This initialise a node with an item provided

        Args:
            value (_type_): It could be any data type
        """
        self.val = item
        self.left = None
        self.right = None

class Tree_Traversal:
    """This class contains an init method and three other method to help explain the three types of traversal we have in tree data structures
    """
    def __init__(self):
        self.root = None

    def inorder(self, root):
        if root:
            # Traverse left
            self.inorder(root.left)
            # Traverse root
            print(str(root.val) + " -> ", end='')
            # Traverse right
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            # Traverse root
            print(str(root.val) + " -> ", end='')
            # Traverse left
            self.preorder(root.left)
            # Traverse right
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            # Traverse left
            self.postorder(root.left)
            # Traverse right
            self.postorder(root.right)
            # Traverse root
            print(str(root.val) + " -> ", end='')

    

#--- EXAMPLE ---#
tree = Tree_Traversal()
tree.root = Node(2)
tree.root.left = Node(4)
tree.root.right = Node(6)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)
tree.root.right.left = Node(7)
tree.root.right.right = Node(10)

print("\n\nInorder traversal ")
tree.inorder(tree.root)

print("\n\nPreorder traversal ")
tree.preorder(tree.root)

print("\n\nPostorder traversal ")
tree.postorder(tree.root)

