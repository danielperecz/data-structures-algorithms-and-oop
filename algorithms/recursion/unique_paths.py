def unique_paths(rows, columns):
    # Returns the number of shortest paths from a grid of size rows * columns.
    # Can move one stop right or one step down at a time.
    if rows == 1 or columns == 1:
        return 1
    return unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)


if __name__ == "__main__":
    print(unique_paths(3, 7))
