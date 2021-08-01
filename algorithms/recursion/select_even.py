def select_even(a):
    # Returns even numbers from an array.
    if not a:
        return []
    else:
        if a[0] % 2 == 0:
            return [a[0]] + select_even(a[1:])
        return select_even(a[1:])


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(select_even(arr))
