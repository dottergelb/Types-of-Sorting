def quicksort_up(arr, i=None):
    if len(arr) <= 1:
        return arr
    support = arr[len(arr) // 2]
    left = [x for x in arr if x < support]
    middle = [x for x in arr if x == support]
    right = [x for x in arr if x > support]
    return quicksort_up(left) + middle + quicksort_up(right)


def quicksort_down(arr, i=None):
    if len(arr) <= 1:
        return arr
    support = arr[len(arr) // 2]
    left = [x for x in arr if x > support]
    middle = [x for x in arr if x == support]
    right = [x for x in arr if x < support]
    return quicksort_down(left) + middle + quicksort_down(right)
