def count_chars(a):
    # Returns total number of characters across all strings within array.
    if not a:
        return 0
    return len(a[0]) + count_chars(a[1:])


if __name__ == "__main__":
    arr = ["ab", "c", "def", "ghij"]
    print(count_chars(arr))
