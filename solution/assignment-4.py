def reverse_string(s):
    # Initialize an empty stack (list)
    stack = []
    
    # Push all characters of the string onto the stack
    for char in s:
        stack.append(char)
    
    # Pop characters from the stack to form the reversed string
    reversed_s = ""
    while stack:
        reversed_s += stack.pop()
    
    return reversed_s

# Example usage:
input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print(f"Reversed string: {reversed_string}")

