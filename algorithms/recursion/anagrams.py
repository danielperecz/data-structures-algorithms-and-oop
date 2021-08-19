def anagrams(s):
    if len(s) == 1:
        return [s]
    collection = []
    for substring in anagrams(s[1:]):
        for i in range(len(substring) + 1):
            collection.append(substring[:i] + s[0] + substring[i:])
    return collection
