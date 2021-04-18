def ft_abs(x: float) -> float:
    return -x if x < 0 else x


def ft_sqrt(n: float) -> float:
    x = 1
    while True:
        nx = (x + n / x) / 2
        if ft_abs(x - nx) < 1e-10:
            break
        x = nx
    return x
