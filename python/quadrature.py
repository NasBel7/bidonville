#coding: utf-8#

import numpy as np

def f(x):
    return x**2

def pt_mil(f,a,b,n):
    """Quadrature de \int_a^b f(x)dx par la méthode du point milieu sur [a,b] découpé en n sous intervalles égaux"""

    h = (b-a)/n
    xm = np.lindspace(a+0.5*h,b-0.5*h,n)
    Q = h*np.sum(f(xm))
    return Q
