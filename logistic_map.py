import numpy as np

import matplotlib.pyplot as plt

from scipy.integrate import odeint

log_map = np.zeros(100)
# print(log_map)


# noinspection PyUnusedLocal
def func(x, t, r):
    return r * x * (1 - x)


time = np.arange(10)

y0 = .01

r0 = 3

y = odeint(func, y0, time, args=(r0,))
print(time)
print([y0, func(y0, time, r0), func(func(y0, time, r0), time, r0)])
print(y[:, 0])
x = y[:, 0]
xn = np.roll(x, -1)
x = np.delete(x, -1)
xn = np.delete(xn, -1)
plt.plot(xn, x)
plt.xlabel('t')
plt.ylabel('y')
plt.show()

#
# plt.scatter(log_map, log_map)
# plt.show()
