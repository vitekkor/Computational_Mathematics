import numpy
from display import pick_step, to_plot, to_table
import lab1.interpolation as interpolation

points = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
points_to_calc = [0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95]


def function(x):
    return 1 / (1 + x)


def integral(x, m):
    return abs(x - numpy.tan(x)) ** m


def compare():
    x_f, y_f = pick_step(function, 0.05, 1.05, 0.1)
    x_l, y_l = pick_step(interpolation.lagrange(function, points), 0.05, 1.05, 0.1)
    x_s, y_s = pick_step(interpolation.spline(function, points), 0.05, 1.05, 0.1)
    print("x\tfunction\tlagrange\teps_lagr")
    for i in range(len(x_f)):
        print(f"{x_f[i]:.2f}\t{y_f[i]:.15f}\t{y_l[i]:.15f}\t{(y_f[i] - y_l[i]):.15f}")
    print(f"x\tfunction\tspline\teps_spline")
    for i in range(len(x_f)):
        print(f"{x_f[i]:.2f}\t{y_f[i]:.15f}\t{y_s[i]:.15f}\t{(y_f[i] - y_s[i]):.15f}")


def lab1(task: int):
    if task == 0:
        to_plot(interpolation.lagrange(function, points), 0.05, 0.95, "lagrange_plot")
        to_table(interpolation.lagrange(function, points), points_to_calc, "lagrange_table")
    if task == 1:
        to_plot(interpolation.spline(function, points), 0.05, 0.95, "Spline_plot")
        to_table(interpolation.spline(function, points), points_to_calc, "Spline_table")
    if task == 2:
        to_plot(function, 0.05, 0.95, "function_plot")
        to_table(function, points_to_calc, "function_table")
        compare()
