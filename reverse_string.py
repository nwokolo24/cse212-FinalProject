def reverser_string(word):
    """This function takes in a string
       and prints out the reverse using
       push() and pop() operation of stack.

    Args:
        word (_type_): string
    """
    # An empty stack to store characters
    # from "word" parameter.
    stack = []

    # A for loop to populate the empty
    # stack with characters from "word".
    for char in word:
        stack.append(char)

    # A for loop to print out these 
    # characters from the stack
    # using pop() operation.
    for i in range(len(word)):
        print(stack.pop(), end='')


word = "love"
reverser_string(word)