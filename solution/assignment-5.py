def is_palindrome(s):
    # Clean the string: remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_s = ''.join(e.lower() for e in s if e.isalnum())
    
    # Use two pointers to check if the string is a palindrome
    left, right = 0, len(cleaned_s) - 1
    
    while left < right:
        if cleaned_s[left] != cleaned_s[right]:
            return False
        left += 1
        right -= 1
        
    return True

# Example usage:
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")

