def index_of_x(s):
    # Returns the index of the first occurrence of the character x.
    if s[0] == "x":
        return 0
    return index_of_x(s[1:]) + 1


def index_of_char(s, c, i=0):
    # Returns the index of the first occurrence of the character c.
    if not s:
        return f"{c} not found."
    else:
        if s[0] == c:
            return i
        return index_of_char(s[1:], c, i + 1)


if __name__ == "__main__":
    test_string = "wesgswgxxge"
    print(index_of_x(test_string))
    print(index_of_char([19, 21, 3], 21))
