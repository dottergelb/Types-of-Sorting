def bin_vstavki_up(a, n):
    for i in range(1, n):
        key = a[i]
        left = 0
        right = i - 1
        while left <= right:
            mid = (left + right) // 2
            if a[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
    for j in range(i - 1, left - 1, -1):
        a[j + 1] = a[j]
        a[left] = key
    return a


def bin_vstavki_down(a, n):
    for i in range(1, n):
        key = a[i]
        left = 0
        right = i - 1
        while left <= right:
            mid = (left + right) // 2
            if a[mid] < key:
                right = mid - 1
            else:
                left = mid + 1
    for j in range(i - 1, left - 1, -1):
        a[j + 1] = a[j]
        a[left] = key
    return a

