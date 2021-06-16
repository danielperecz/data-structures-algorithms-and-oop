def bubble_sort(a):
    n = len(a)
    i = 0
    while i < n:
        j = 0
        while j < n - 1:
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            j += 1
        i += 1
