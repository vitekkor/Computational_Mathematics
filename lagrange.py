# math
import numpy


def lagrange(fun, points: list, points_to_calc: list):
    z = numpy.zeros(len(points_to_calc))
    for point in range(len(points_to_calc)):
        for j in range(len(points)):
            l1 = 1
            l2 = 1
            for i in range(len(points)):
                if i != j:
                    l1 = l1 * (points_to_calc[point] - points[i])
                    l2 = l2 * (points[j] - points[i])

            z[point] = z[point] + fun(j) * l1 / l2
    return z
