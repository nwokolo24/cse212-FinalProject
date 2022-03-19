# Python program to check for
# balanced brackets.
 
# function to check if
# brackets are balanced
 
 
def balanced_brackets(expr):
    """This function checks if brackets
       contained in the "expr" are balanced
       or not.

    Args:
        expr (_type_): string

    Returns:
        _type_: boolean
    """
    stack = []
 
    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "["]:
 
            # Push the element in the stack
            stack.append(char)
        else:
            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            
            #Implement your code below

 
    # Check Empty Stack
    if stack:
        return False
    return True
 
 
# Driver Code
if __name__ == "__main__":
    expr = "{()}[]"
 
    # Function call
    if balanced_brackets(expr):
        print("Balanced")
    else:
        print("Not Balanced")