memo = {0: 0, 1: 1}


def fibonacci(n):
    if n not in memo:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]
