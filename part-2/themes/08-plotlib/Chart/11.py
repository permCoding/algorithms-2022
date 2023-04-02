import matplotlib.pyplot as plt


numsides = [3, 4, 5, 6, 7, 8, 9, 10, 11]
squares = [
    4330.13, 10000.0, 17204.77, 
    25980.76, 36339.12, 48284.27, 
    61818.24, 76942.09, 93656.4
]

plt.xlabel('Количество сторон')
plt.ylabel('Площадь')

plt.plot(numsides, squares, '--og', lw=2)

plt.show()

'''

если размер одной стороны равен 100, 
то площади фигур с количеством сторон
3 4 5 6 7 .. будут равны:
#
#
#

а как будет зависеть площадь фигуры от её периметра?
'''
