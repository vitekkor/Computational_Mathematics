# math
import numpy
# for splines
from scipy import integrate


def integrate_newton_cotes(func, a, b):
    """
        Calculates an integral of `func`
        for t = a..b via newton-cotes of order 9.
        """
    # the order of newton-cotes
    # formulas (number of points)
    n = 9

    # the 9 sample points
    x = numpy.linspace(a, b, n)

    # get newton-cotes coefficients
    # for the order n
    a_, b_ = integrate.newton_cotes(n - 1)
    result = 0

    for it in range(n):
        result += a_[it] * func(x[it])

    # multiply by the average step
    result *= (b - a) / (n - 1)
    return result


def quanc8(func, a, b, ai, bi, abs_error, rel_error, rough=None):
    """
    Simulates QUANC8.
    `func` is the function we integrate.
    `rough` is an approximation of the a..b integral and
    will only be calculated at the 'root' call of quanc8
    recursion tree.
    """
    middle = (ai + bi) / 2

    p = integrate_newton_cotes(func, ai, bi)
    p1 = integrate_newton_cotes(func, ai, middle)
    p2 = integrate_newton_cotes(func, middle, bi)
    q = p1 + p2

    error = numpy.abs((q - p) / 1023)
    h = bi - ai

    if rough is None:
        rough = p

    if error <= h / (b - a) * numpy.max([abs_error, rel_error * rough]):
        return q

    return quanc8(func, a, b, ai, middle, abs_error, rel_error, rough) + \
           quanc8(func, a, b, middle, bi, abs_error, rel_error, rough)
