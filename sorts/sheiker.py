def shaker_up(a, i=None):
    left = 0
    right = len(a) - 1
    while left <= right:
        for i in range(left, right):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        right = -1
        for i in range(right, left, -1):
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
        left += 1
    return a


def shaker_down(a, i=None):
    left = 0
    right = len(a) - 1
    while left <= right:
        for i in range(left, right):
            if a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        right = -1
        for i in range(right, left, -1):
            if a[i - 1] < a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
        left += 1
    return a



