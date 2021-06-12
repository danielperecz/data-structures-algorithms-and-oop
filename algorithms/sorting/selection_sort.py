def selection_sort(a):
    i = 0
    while i < len(a):

        # Find minimum element in remaining list.
        j_min = i
        j = i + 1
        while j < len(a):
            if a[j] < a[j_min]:
                j_min = j
            j += 1

        # Swap elements.
        if j_min != i:
            a[i], a[j_min] = a[j_min], a[i]

        i += 1
