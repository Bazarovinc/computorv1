ft_abs = lambda x: -x if x < 0 else x


def sqrt(n):
    x = 1
    while True:
        nx = (x + n / x) / 2
        if ft_abs(x - nx) < 1e-10:
            break
        x = nx
    return x

print(sqrt(123))