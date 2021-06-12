def swap(i, a):
    # Swap neighbours.
    a[i], a[i + 1] = a[i + 1], a[i]


def bubble_sort(a):
    n = len(a)
    i = 0
    while i < n:
        j = 0
        while j < n - 1:
            if a[j] > a[j + 1]:
                swap(j, a)
            j += 1
        i += 1
