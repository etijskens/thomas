# -*- coding: utf-8 -*-

"""
## Python package thomas
"""

__version__ = '0.0.0'

from math import sqrt

def append_w(ll, w):
    result = []
    for l in ll:
        result += [ l + [w], l + [-w] ]
    return result

def lijst_wortels(a):
    w = sqrt(a[-1])
    if len(a) == 1:
        return [[w], [-w]]
    else:
        ww = lijst_wortels(a[:-1])
        ww =  append_w(ww, w)
        return ww

import numpy as np

def kwantiseer(a, q):
    q = np.sort(q)
    ip = np.searchsorted(q, a)
    # if isinstance(ip, np.ndarray):
    #     ip[ip==len(q)] = len(q)-1
    # else:
    #     if ip == len(q):
    #         ip = len(q)-1
    return q[ip]

if __name__ == "__main__":
    # print(lijst_wortels([2.0,3.0]))
    a = np.linspace(-5,5,21)
    q = [-3.0,-1.0,-2.0,1.0,3.0,4.0,2.0]
    print(kwantiseer(a, q))
    a = -1.2
    print(kwantiseer(a, q))
