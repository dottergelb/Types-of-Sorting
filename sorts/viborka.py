def vibor_up(a, n):
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a


def vibor_down(a, n):
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    return a



