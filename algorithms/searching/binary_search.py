import math


def binary_search(a, t):
    if len(a) > 0:
        left = 0
        right = len(a) - 1
        while left != right:
            m = math.ceil((left + right) / 2)
            if a[m] > t:
                right = m - 1
            else:
                left = m
        if a[left] == t:
            return left
    return "Unsuccessful"
