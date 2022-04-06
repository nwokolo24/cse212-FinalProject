# Table of Contents
- [Introduction](#introduction)
- [Tree Terminologies](#tree-terminologies)
- [Types of Tree Data Structure](#types-of-tree-data-structure)
- [Tree Traversal](#tree-traversal)
- [Binary Search Tree](#binary-search-tree)
- [Basic BST Operation Implementation](#basic-bst-operation-implementation)
- [Exercises](#exercises)

# Introduction
A tree is a non-linear data structure consisting of a collection of nodes connected by directed or undirected edges. A tree data structure can be empty(containing no node), it can contain a single node called the root node or it can contain a root and other sub nodes or subtrees.
# Tree Terminologies
In this subsection, we will be learning about some basic terminologies that are common when working with tree data structures.
- **Node:** A node is an element of a tree. It contains a value and pointer to its child nodes.

- **Leaf:** If a node does not contain a pointer to a child node, then that node can be referred to as a leaf node, in other words, any node that does not have a child is called a leaf node. The pointers of leaf nodes usually points to None or Null.

- **Root:** The topmost node of a tree is the root node. The root node can also be seen at the element of a tree data structure that determines which sides of the tree a node goes, depending on the content or data or value of such node.

- **Edge:** In tree data structure, edge is the link between two nodes.

- **Child Node:** If a node is a lead to another node, then that node is a child to the node to which it is a leaf.

- **Parent Node:** As you might be thinking, a node that has leaf is parent to that leaf. That means the parent node has an edge to a child node.

- **Height of a Tree:** The height of a tree is the number of nodes from the root node to the deepest leaf.

- **Height of a Node:** The height of a node is the number of edges from that node to the deepest leaf.

- **Dept of a Node:** The dept of a node is the number of edges from the root nood to that node.

Here is a picture illustrating some of these terminologies
![Tree Terminologies](tree_terminologies.png)
Photo Credit: upgrad.com

# Types of Tree Data Structure
Here are some common types of tree data structures
- **General Tree**
- **Binary Tree**
- **Binary Search Tree**
- **AVL Tree**
- **Red Black**
- **B-Tree**
# Tree Traversal
Traversing a tree entails visiting all of its nodes. There is just one way to read data in linear data structures like arrays, stacks, queues, and linked lists. A tree, on the other hand, is a hierarchical data structure that may be traversed in a variety of ways. These ways includes:
- **Inorder traversal:** 
    - Visit all nodes in the left subtree
    - Then visit the root node
    - Lastly, visit the all nodes in the right subtree
- **Preorder traversal:**
    - Visit the root node
    - Visit all nodes in the left subtree
    - Visit all nodes in the right subtree 
- **Postorder traversal:**
    - Visit all nodes in the left subtree
    - Visit all nodes in the right subtree
    - Visit the root node

Click this [link](tree_traversal.py) to see am example of the inplementation of the three types of traversal in Tree Data Structure.

# Binary Search Tree
Before we expalain what a binary search tree is, it will be nice to know what a binary tree is.

>A binary tree is a tree data structure in which each parent node can have at most two children. 

>Binary search tree which is an example of binary tree, is a data structure that quickly allows us to maintain a sorted list of numbers.

According to cse212 course material, "A binary search tree (BST) is a binary tree that follows rules for data that is put into the tree. Data is placed into the BST by comparing the data with the value in the parent node. If the data being added is less than the parent node, then it is put in the left subtree. If the data being added is greater than the parent node, then it is put in the right subtree. If duplicates are allowed than the duplicate can be put either to the left or to the right of the root. By using this process, the data is stored in the tree sorted."

Three characteristics that seperates BST from other types of binary trees are:
- All nodes of left subtree are less than the root node.
- All nodes of right subtree are greater than the root node.
- Both subtrees of each node are also BSTs, that is they have the two properties above.

**BST Search Algorithm**

Here is a representation of the algorithm for searching a BST
```python
If root == None 
    return None;
If value == root.data 
    return root.data;
If value < root.data 
    return search(root.left)
If value > root.data 
    return search(root.right)
```

**BST Insert Algorithm**

```python
If node == None 
    return create_node(value)
if (value < node.value)
    node.left  = insert(node.left, value);
else if (value > node.value)
    node.right = insert(node.right, data);  
return node;
```

A picture representation of this explanaton
![Binary Search Tree](bst.png)
Photo Credit: cse212 course material

As we shall see in the example below, here is a pictoral representation of Binary Search Tree Operations.
![BST Operations](bst_operation.png)
Photo Credit: cse212 course material

# Basic BST Operation Implementation
Here is [link](bst_operations.py) showing some bst operations.
Credit: The example in the link above is from programiz.com and clearly explained important bst operations.

# Exercises
**QUESTION**
Here is an industry standard [exercise](tree_exercise.py) to help you practice BST. Here is a [solution](tree_exercise_solution.py) to the exercise

[Back to top](#table-of-contents)
