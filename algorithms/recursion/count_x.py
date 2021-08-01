def count_x(s):
    # Function counts x characters in string.
    if not s:
        return 0
    if s[0] == "x":
        return 1 + count_x(s[1:])
    return count_x(s[1:])
