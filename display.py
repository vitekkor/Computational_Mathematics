# для рисования
from matplotlib import pyplot, ticker
import pandas
# math
import numpy


def pick(fun, a, b, count):
    x = numpy.linspace(a, b, count)
    y = fun(x)
    return x, y


def pick_step(fun, a, b, step):
    x = numpy.arange(a, b, step)
    y = fun(x)
    return x, y


def to_plot(fun, a: float, b: float, title: str,
            count: int = 1000, save: bool = 1, major_xaxis: float = 0.1, minor_xaxis: float = 0.05,
            major_yaxis: float = 0.05, minor_yaxis: float = 0.1):
    x, y = pick(fun, a, b, count)
    pic, ax = pyplot.subplots()
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
    if save:
        pyplot.savefig(f"{title}.png")
    pyplot.show()


def to_table(fun, table_points: list, title: str, save: bool = 1):
    fig, ax = pyplot.subplots()

    # hide axes
    ax.axis('off')
    ax.axis('tight')

    y = []
    for x in table_points:
        y.append(fun(x))
    data = []
    for x in table_points:
        data.append([x, y[table_points.index(x)]])

    df = pandas.DataFrame(data, columns=list('xy'))

    ax.table(cellText=df.values, colLabels=df.columns, loc='center')

    pyplot.title(title)
    fig.tight_layout()
    if save:
        pyplot.savefig(f"{title}.png")
    pyplot.show()
