import numpy as np
cimport numpy as np
cimport cython


DTYPE = np.int
# "ctypedef" assigns a corresponding compile-time type to DTYPE_t. For
# every type in the numpy module there's a corresponding compile-time
# type with a _t-suffix.
ctypedef np.int_t DTYPE_t

def func(double x, double r):
    return r * x * (1 - x)

@cython.boundscheck(False)
def iterate(double x0, int n_iters, int x_iters, double r, double eps):
    cdef np.ndarray[double, ndim=2] x = np.zeros([x_iters, n_iters], dtype=np.double)
    x[0,0] = x0

    for n in range(1, n_iters):
        for x_n in range(0, x_iters-1):
            next_iter = (x_n + 1) if x_iters > x_n + 1 else 0
            left_nbr = x_n - 1 if x_n > 0 else x_iters - 1
            x[x_n,n] = (1 - 2* eps) * func(x[0,n-1], r) + eps * func(x[x_n + 1, n-1], r) + eps * func(x[x_n - 1, n-1], r)

    return x