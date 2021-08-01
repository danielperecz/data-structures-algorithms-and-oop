def triangular_num(n):
    # Returns the triangular number for the given n. Sequence begins 0, 1, 3, 6, 10, 15, 21, 28.
    if n == 0 or n == 1:
        return n
    return n + triangular_num(n - 1)


if __name__ == "__main__":
    print(triangular_num(7))
