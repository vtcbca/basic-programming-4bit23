def print_triangle_3(n):
    for i in range(1, n + 1):
        # Create the row using list comprehension
        row = [str(x) for x in range(1, 2 * i)]
        
        # Print leading spaces for centering
        print(" " * (n - i) + " ".join(row))

# Example usage:
n = 4
print_triangle_3(n)

