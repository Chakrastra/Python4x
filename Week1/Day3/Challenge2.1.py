# Factorial by using Iterative method
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n=input("Enter number:")

if not n.isdigit() or int(n)<0:
    print("Enter a valid number")
else:
    
    print(f"\nFactorial of {n} is:{factorial(int(n))}")
    
