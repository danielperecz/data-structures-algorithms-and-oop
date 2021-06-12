def _qsort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        _qsort(a, low, pivot)
        _qsort(a, pivot + 1, high)


def partition(a, low, high):
    # Partition using Hoare partition scheme.
    pivot = a[low]
    while True:
        while a[low] < pivot:
            low += 1

        while a[high] > pivot:
            high -= 1

        if low >= high:
            return high

        a[low], a[high] = a[high], a[low]
        low += 1
        high -= 1


def quick_sort(a):
    _qsort(a, 0, len(a) - 1)
