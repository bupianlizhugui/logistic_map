import numpy as np

import matplotlib.pyplot as plt

from scipy.integrate import odeint
import time

import iterate

start = time.time()

xx = iterate.iterate(.1, 100000, 3, 4, .3)

print(np.array(xx))

r0 = 3

end = time.time()
print(end - start)

xn = np.roll(xx, -1)
x = np.delete(xx, -1)
xn = np.delete(xn, -1)

plt.scatter(x, xn, marker='.')
plt.xlabel('x[n]')
plt.ylabel('x[n+1]')
plt.show()

#
# plt.scatter(log_map, log_map)
# plt.show()
