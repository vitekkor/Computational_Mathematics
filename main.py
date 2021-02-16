import interpolation
import numpy
from display import to_table
from display import to_plot

points = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
points_to_calc = [0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95]


def function(x):
    return 1 / (1 + x)


def integral(x, m):
    return abs(x - numpy.tan(x)) ** m


if __name__ == '__main__':
    # to_plot(interpolation.lagrange(function, points), 0.05, 0.95, "lagrange")
    # to_plot(interpolation.spline(function, points), 0.05, 0.95, "Spline")

    # to_table(interpolation.lagrange(function, points), points_to_calc, "lagrange")
    # to_table(interpolation.spline(function, points), points_to_calc, "Spline")
    print()
