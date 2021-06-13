import math


def binary_search(a, t):
    if len(a) > 0:
        left = 0
        right = len(a) - 1
        while left != right:
            mid = math.ceil((left + right) / 2)
            if a[mid] > t:
                right = mid - 1
            else:
                left = mid
        if a[left] == t:
            return left
    return "Unsuccessful"
