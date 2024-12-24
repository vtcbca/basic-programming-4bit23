def print_pattern_2(n):
    for i in range(1, n + 1):
        # Generate increasing letters
        increasing = [chr(64 + j) for j in range(1, i + 1)]
        
        # Generate decreasing letters
        decreasing = increasing[:-1][::-1]
        
        # Join both parts and print with leading spaces
        row = " ".join(increasing + decreasing)
        print(" " * (n - i) + row)

# Example usage:
n = 3
print_pattern_2(n)

