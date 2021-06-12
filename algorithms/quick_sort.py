def _qsort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        _qsort(a, low, pivot)
        _qsort(a, pivot + 1, high)


def partition(a, low, high):
    # Partition using Hoare partition scheme.
    pivot = a[low]
    i = low
    j = high
    while True:
        while a[i] < pivot:
            i += 1

        while a[j] > pivot:
            j -= 1

        if i >= j:
            return j

        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1


def quick_sort(a):
    _qsort(a, 0, len(a) - 1)
