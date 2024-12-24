def sieve_of_eratosthenes(limit):
    # Initialize a boolean array to track primes
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    
    return primes

def is_prime(n, primes):
    if n < len(primes):
        return primes[n]
    return False

# Example usage:
limit = int(input("Enter the upper limit for primes: "))
primes = sieve_of_eratosthenes(limit)

number = int(input("Enter a number to check if it's prime: "))
if is_prime(number, primes):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

