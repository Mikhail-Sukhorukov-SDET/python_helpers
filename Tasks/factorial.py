def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *=i
    return fact
print(factorial(5))

def fact(n):
    if n == 1:
        return 1
    return fact(n-1) * n
print(fact(4))