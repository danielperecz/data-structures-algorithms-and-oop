def insertion_sort(a):
    if len(a) > 1:
        i = 1
        while i < len(a):
            x = a[i]
            j = i - 1
            while j >= 0 and a[j] > x:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = x
            i += 1
