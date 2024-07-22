
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
def is_prime(n):
    if n <= 1:
        return "Not prime"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "Not prime"
    return "Prime"

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]
