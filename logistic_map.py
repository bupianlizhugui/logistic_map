import time

import matplotlib.pyplot as plt
import numpy as np

import iterate

start = time.time()

# todo iterate R
xx = iterate.iterate(.1, 100, 5, 2, .5)

print(np.array(xx))

end = time.time()
print(end - start)

xn = np.roll(xx, -1)
x = np.delete(xx, -1)
xn = np.delete(xn, -1)

# plt.scatter(x, xn, marker='.')
# plt.xlabel('x[n]')
# plt.ylabel('x[n+1]')
# plt.show()
print(xx.shape)

plt.scatter(np.arange(xx.shape[1]), xx[0], marker='.')
plt.xlabel('x[n]')
plt.ylabel('x[n+1]')
plt.show()

#
# plt.scatter(log_map, log_map)
# plt.show()
