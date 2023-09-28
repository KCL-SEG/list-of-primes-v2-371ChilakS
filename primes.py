"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Negative numbers and zero are invalid inputs")
    
    list = []
    number = 2
    while len(list)<number_of_primes:
        if is_prime(number):
            list.append(number)
        number+=1
    return list

def is_prime(number):
    if number < 2:
        return False
    for counter in range(2,int(number**0.5)+1):
        if number % counter == 0:
            return False
    return True

# print(
#     f'negative input -> {primes(-12)}'
#     f'negative input -> {primes(-1)}'
#     f'0 input -> {primes(0)}'
#     f'1 input -> {primes(1)}\n'
#     f'5 input -> {primes(5)}\n'
#     f'10 input -> {primes(10)}\n'
# )
