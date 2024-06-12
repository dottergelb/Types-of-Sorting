def shell_up(a, i=None):
    n = len(a)
    g = n // 2
    while g > 0:
        for i in range(g, n):
            p = a[i]
            j = i
            while j >= g and a[j - g] > p:
                a[j] = a[j - g]
                j -= g
            a[j] = p
        g //= 2
    return a


def shell_down(a, i=None):
    n = len(a)
    g = n // 2
    while g > 0:
        for i in range(g, n):
            p = a[i]
            j = i
            while j >= g and a[j - g] < p:
                a[j] = a[j - g]
                j -= g
            a[j] = p
        g //= 2
    return a
