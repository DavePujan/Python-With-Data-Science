# problems.py - Function based problems

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print("5! =", factorial(5))
