# Converting an array to a linked list
 
# Representation of a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
# Function to insert node
def insert(root, item):
    temp = Node(item)
     
    if (root == None):
        root = temp
    else :
        pointer = root
        while (pointer.next != None):
            pointer = pointer.next
        pointer.next = temp
     
    return root
 
def display(root):
    while (root != None) :
        print(root.data, end = " ")
        root = root.next
         
def arrayToList(arr, n):
    root = None
    for i in range(0, n, 1):
        root = insert(root, arr[i])
     
    return root

arr = [1, 2, 3, 4, 5]
n = len(arr)
root = arrayToList(arr, n)
display(root)


# Solution to exercise
def reverseList(node):
    new_array = []
    prev = None
    curr = node
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    return prev

reverse = reverseList(root)
display(reverse)


# Sources of question and answer implementation
# geeksforgeeks.com
# leetcode.com