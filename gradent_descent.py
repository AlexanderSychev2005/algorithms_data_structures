import matplotlib.pyplot as plt
import time
import numpy as np
import matplotlib

def f(x):
  return x**2 - 5*x + 5

def df(x):
  return 2*x - 5

N = 20
xx = 0 # начальное значение
alpha = 0.1 # Шаг сходимости

x_plt = np.arange(0, 5, 0.1)
f_plt = f(x_plt)


plt.ion()
fig, ax = plt.subplots()
ax.grid()

ax.plot(x_plt, f_plt)
points = ax.scatter(xx, f(xx), color="red")

for i in range(N):
  xx = xx - alpha * df(xx)
  points.set_offsets([xx, f(xx)])


  fig.canvas.draw()
  fig.canvas.flush_events()
  time.sleep(0.02)

plt.ioff()
print(xx)
ax.scatter(xx, f(xx), c='blue')
plt.show()