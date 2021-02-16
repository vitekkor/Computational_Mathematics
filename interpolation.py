# for splines
from scipy import interpolate


def lagrange(fun, points: list):
    y = []
    for point in points:
        y.append(fun(point))
    return interpolate.lagrange(points, y)


def spline(fun, points: list):
    y = []
    for point in points:
        y.append(fun(point))
    return interpolate.CubicSpline(points, y)
