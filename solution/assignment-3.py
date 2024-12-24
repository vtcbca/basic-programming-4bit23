def fibonacci_max_value(max_val):
    # Initialize the Fibonacci sequence
    fib_sequence = []
    
    # First two Fibonacci numbers
    a, b = 0, 1
    
    # Generate Fibonacci numbers until the max value is reached
    while a <= max_val:
        fib_sequence.append(a)
        a, b = b, a + b  # Move to the next pair of Fibonacci numbers
    
    return fib_sequence

# Example usage:
max_val = int(input("Enter the maximum value: "))
print(f"Fibonacci sequence up to {max_val}: {fibonacci_max_value(max_val)}")

