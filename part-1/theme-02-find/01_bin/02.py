import matplotlib.pyplot as plt


def func(x):
    return 9.5*x**3 - 500


plt.style.use('seaborn')

left, right, count = -5, 5, 1000  # точность зависит от кол-ва точек
x, step = left, (right - left) / count

lst_x, lst_y = [], []
while x < right:
    lst_x.append(x)
    lst_y.append(func(x))
    x += step

fig, axes = plt.subplots()
axes.vlines(0, min(lst_y), max(lst_y), color='orange', lw=2)
axes.hlines(0, min(lst_x), max(lst_x), color='orange', lw=2)
axes.plot(lst_x, lst_y, color='darkviolet', lw=4)

plt.show()
