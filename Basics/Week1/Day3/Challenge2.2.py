# Factorial by using Recursive method
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n=input("Enter number:")

if not n.isdigit() or int(n)<0:
    print("Enter a valid number")
else:
    
    print(f"\nFactorial of {n} is:{factorial(int(n))}")
    
