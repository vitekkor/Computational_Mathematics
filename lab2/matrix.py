from numpy import array, ndarray, linalg
from scipy.linalg import lu_factor, lu_solve


def get_a(p: float) -> ndarray:
    return array([[p - 29, 6, -6, -4, -3, -8, -5, 5],
                  [6, -13, -3, 5, 4, 3, 1, 7],
                  [5, -5, -1, 7, 2, 0, 7, 1],
                  [5, -5, 5, 6, 4, -7, 4, 0],
                  [4, 4, 7, -4, 9, -8, -8, -4],
                  [-4, 5, -4, 1, 0, 12, 0, 6],
                  [-3, -2, -4, 2, -8, -3, 16, 4],
                  [7, 5, 0, 2, 0, -6, 8, -12]])


def get_b(p: float) -> ndarray:
    return array([4 * p - 175, 133, 110, 112, 17, 32, 13, -18])


def solve_matrix_equation1(p: float):
    a = get_a(p)
    b = array([4 * p - 175, 133, 110, 112, 17, 32, 13, -18])
    lu, piv = lu_factor(a, check_finite=False)
    return a, lu_solve((lu, piv), b, check_finite=False)


def solve_matrix_equation2(p: float):
    a = get_a(p)
    a_t = a.T
    a = a_t.__matmul__(a)
    b = a_t.__matmul__(get_b(p))
    lu, piv = lu_factor(a, check_finite=False)
    return lu_solve((lu, piv), b, check_finite=False)


def cond_delta(a: ndarray, x1: ndarray, x2: ndarray):
    cond = linalg.cond(a)
    delta = linalg.norm(x1.__sub__(x2)) / linalg.norm(x1)
    return cond, delta


def compare_result(a: ndarray, x1: ndarray, x2: ndarray):
    print("x\tEquation1\tEquation1\teps")
    for i in range(x1.__len__()):
        print(f"{i + 1}\t{x1[i]}\t{x2[i]}\t{x1[i] - x2[i]}")
    print()
    cond, delta = cond_delta(a, x1, x2)
    print(f"Cond\t{cond}")
    print(f"Delta\t{delta}")


def lab2():
    p_list = [1.0, 0.1, 0.01, 0.0001, 0.000001]
    for p in p_list:
        a, x1 = solve_matrix_equation1(p)
        x2 = solve_matrix_equation2(p)
        print(f"p = {p}")
        compare_result(a, x1, x2)
