import numpy
from matplotlib import pyplot
from scipy import integrate

from display import pick_step


def lab3():
    evaluate(h=0.1)
    evaluate(h=0.05)
    evaluate(h=0.025)
    evaluate(h=0.0125)


def rkf45(fun, t, y0):
    r = (integrate.ode(fun)
         .set_integrator('dopri5')
         .set_initial_value(y0, t[0]))

    y = numpy.zeros((len(t), len(y0)))
    y[0] = y0

    for it in range(1, len(t)):
        y[it] = r.integrate(t[it])

        if not r.successful():
            raise RuntimeError('Couldn\'t integrate')

    return y[:, 0]


def f(t, y):
    d_y = numpy.zeros(y.shape)
    d_y[0] = y[1]
    d_y[1] = -1.0 * y[1] / (2.0 * t)
    return d_y


def g(t):
    return 2.0 * numpy.sqrt(t)


def euler_cauchy(fun, t, y0):
    h = t[1] - t[0]
    y = numpy.zeros((len(t), len(y0)))
    # calculate

    y[0] = y0
    for i in range(1, len(t)):
        y1 = y[i - 1] + h * fun(t[i - 1], y[i - 1])
        y[i] = y[i - 1] + h * (fun(t[i - 1], y[i - 1]) + fun(t[i], y1)) / 2.0
    return y[:, 0]


def evaluate(h=0.1):
    # range
    a = 1.0
    b = 2.0

    # initial conditions
    y0 = numpy.array([2, 1])

    pyplot.title(f'h={h}; Green - exact; Red - RKF45; Blue - Euler_Cauchy')

    t, y_exact = pick_step(g, a, b + h, step=h)
    pyplot.plot(t, y_exact, 'g-')

    y_rkf45 = rkf45(f, t, y0)
    pyplot.plot(t, y_rkf45, 'r--')

    y_euler_cauchy = euler_cauchy(f, t, y0)
    pyplot.plot(t, y_euler_cauchy, 'b--')

    pyplot.show()

    error_local_rkf45 = numpy.abs(y_rkf45 - y_exact)
    error_local_euler_cauchy = numpy.abs(y_euler_cauchy - y_exact)

    print('First step of RKF45:', error_local_rkf45[1])
    print('First step of Euler-Cauchy:', error_local_euler_cauchy[1])

    print('Global of RKF45:', error_local_rkf45.sum())
    print('Global of Euler-Cauchy:', error_local_euler_cauchy.sum())

    print('h^3 is about:', h ** 3)
    print('h^3 / euler first step:', h ** 3 / error_local_euler_cauchy[1])

    print('\tValues')
    print('t\tExact\tRKF45\tEuler-Cauchy')

    for it in range(0, len(t)):
        print('{:0.4f}\t{}\t{}\t{}'.format(t[it], y_exact[it], y_rkf45[it], y_euler_cauchy[it]))
