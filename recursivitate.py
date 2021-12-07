def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


"""
fibo(5) = fibo(4)                                          + fibo(3)
        = fibo(3)            + fibo(2)            + fibo(2)         + fibo(1)
        = fibo(2) + fibo(1) + fibo(1) + fibo(0) + fibo(1) + fibo(0) + 1
        = fibo(2) + 1       + 1       + 0       + 1       + 0       + 1
        = fibo(1) + fibo(0) + 4
        = 1 + 0 + 4
        = 5
"""

print(fibonacci(5))
