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
def iterate(double x0, int n_iters, double r):
    cdef np.ndarray[double, ndim=1] x = np.zeros(n_iters, dtype=np.double)
    x[0] = x0

    for n in range(1, n_iters):
        x[n] = func(x[n-1], r)

    return x