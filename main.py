# для рисования
from matplotlib import pyplot, ticker
# math
import numpy
import pandas
import lagrange

points = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]


def function(x: float):
    return 1 / (1 + x)


def pick(fun, a, b, count):
    x = numpy.linspace(a, b, count)
    y = fun(x)
    return x, y


def to_plot(fun, a: float, b: float, title: str, count: int = 1000, major_xaxis: float = 0.1, minor_xaxis: float = 0.05,
            major_yaxis: float = 0.05, minor_yaxis: float = 0.1):
    x, y = pick(fun, a, b, count)
    ax = pyplot.subplots()[1]
    pyplot.title(title)
    pyplot.plot(x, y, 'b-')
    #  Устанавливаем интервал основных делений:
    ax.xaxis.set_major_locator(ticker.MultipleLocator(major_xaxis))
    #  Устанавливаем интервал вспомогательных делений:
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(minor_xaxis))

    #  Тоже самое проделываем с делениями на оси "y":
    ax.yaxis.set_major_locator(ticker.MultipleLocator(major_yaxis))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(minor_yaxis))

    #  Включаем видимость вспомогательных делений:
    ax.minorticks_on()
    pyplot.show()


def to_table(fun, a: float, b: float, title: str, count: int = 10):
    fig, ax = pyplot.subplots()

    # hide axes
    ax.axis('off')
    ax.axis('tight')

    x, y = pick(fun, a, b, count)
    x = x.tolist()
    y = y.tolist()
    data = []
    for xx in x:
        data.append([xx, y[x.index(xx)]])

    df = pandas.DataFrame(data, columns=list('xy'))

    ax.table(cellText=df.values, colLabels=df.columns, loc='center')

    pyplot.title(title)
    fig.tight_layout()
    pyplot.show()


if __name__ == '__main__':
    to_plot(lambda points_to_calc: lagrange.lagrange(function, points, points_to_calc), 0.05, 0.95, "lagrange")
    to_table(lambda points_to_calc: lagrange.lagrange(function, points, points_to_calc), 0.05, 0.95, "lagrange")
