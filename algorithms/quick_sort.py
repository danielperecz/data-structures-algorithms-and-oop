def _qsort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        _qsort(a, low, pivot)
        _qsort(a, pivot + 1, high)


def partition(a, low, high):
    pivot = a[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        j -= 1

        while a[i] < pivot:
            i += 1

        while a[j] > pivot:
            j -= 1

        if i >= j:
            return j

        a[i], a[j] = a[j], a[i]


def quick_sort(a):
    # Quick sort using Hoare partition scheme.
    _qsort(a, 0, len(a) - 1)
