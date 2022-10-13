import math


def f(x):
    # return 9.5 * x**3 - 500
    return 9.5 * math.pow(x, 3) - 500


eps = .001
a, b = -5, 5
while True:
    middle = a + (b-a) / 2
    y = f(middle)
    if abs(y) < eps:
        print(middle)
        print(y)
        break
    if y > 0:
        b = middle
    else:
        a = middle
