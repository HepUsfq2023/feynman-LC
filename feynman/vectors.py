
import numpy as np
import matplotlib as mpl


def add(vlist, v):
    """
    Add a vector v to a list of vectors.

    Arguments
    ---------

    vlist : np.ndarray of shape (N, l).

    v : np.ndarray of shape (l,)

    Returns
    -------

    vlist2 : np.array of shape (N, l)
 
"""
    assert vlist.ndim == 2, "Wrong dimensions for vlist" 
    assert v.ndim == 1, "Wrong dimensions for v" 
    assert vlist.shape[1] == v.shape[0], "Vectors are not aligned."

    n, l = vlist.shape
    vt = np.tile(v, (n, 1))
    return vlist + vt



def dot(vlist, v):
    """
    Multiply a list of vectors piecewise by each components of v.

    Arguments
    ---------

    vlist : np.ndarray of shape (N, l).

    v : np.ndarray of shape (N,)

    Returns
    -------

    vlist2 : np.array of shape (N, l)
 
"""
    assert vlist.ndim == 2, "Wrong dimensions for vlist" 
    assert v.ndim == 1, "Wrong dimensions for v" 
    assert vlist.shape[0] == v.shape[0], "Vectors are not aligned."

    n, l = vlist.shape
    vt = np.tile(v, (l, 1)).transpose()
    return vlist * vt


def sqdot(vlist, M):
    """
    Multiply each vector of a list by a square matrix M.

    Arguments
    ---------

    vlist : np.ndarray of shape (N, l).

    M : np.ndarray of shape (l, l)

    Returns
    -------

    vlist : np.array of shape (N, l)
 
"""
    assert vlist.ndim == 2, "Wrong dimensions for vlist" 
    assert M.ndim == 2, "Wrong dimensions for v" 
    assert vlist.shape[1] == M.shape[0] == M.shape[1], "Matrices not aligned."

    return np.dot(M, vlist.transpose()).transpose()


