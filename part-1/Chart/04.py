import matplotlib.pyplot as plt
import numpy as np
import math
  
X = np.arange(0, math.pi*2, 0.05)
Y1, Y2, Y3, Y4 = np.sin(X), np.cos(X), np.tan(X), np.tanh(X)
  
figure, axis = plt.subplots(2, 2)  # разбить оси по строкам и столбцам
  
axis[0, 0].plot(X, Y1)
axis[0, 0].set_title("Синус")
  
axis[0, 1].plot(X, Y2)
axis[0, 1].set_title("Косинус")
  
axis[1, 0].plot(X, Y3)
axis[1, 0].set_title("Тангенс")
  
axis[1, 1].plot(X, Y4)
axis[1, 1].set_title("Арктангенс")
  
plt.show()
