# Creating a string of prime numbers
prime_string = ""

# Finding the primes until the length of the string is 10005
i = 2
while len(prime_string) < 10005:
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_string += str(i)
    i += 1

def solution(n):
    # Returning the next five digits in the string
    return prime_string[n:n+5]