def reverse_string_1(s):
    if len(s) == 1:
        return s
    return s[-1] + reverse_string_1(s[:-1])


def reverse_string_2(s):
    if len(s) == 1:
        return s
    return reverse_string_2(s[1:]) + s[0]
