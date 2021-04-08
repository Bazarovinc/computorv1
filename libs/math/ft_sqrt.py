from libs.math.constants import SQRT_PRECISION


def ft_abs(a):
    return -a if a < 0 else a


def f(w, g):
    return g * g - w


def f_prime(g):
    return 2 * (g ** (2 - 1))


def close_enough(a, b):
    return ft_abs(a - b) < ft_abs(b * SQRT_PRECISION)


def find_root(w, g):
    new_guess = g - f(w, g) / f_prime(g)
    if close_enough(new_guess, g):
        return new_guess
    else:
        return find_root(w, new_guess)


def ft_sqrt(w):
    return find_root(w, 1)
