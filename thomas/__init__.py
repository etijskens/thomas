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

if __name__ == "__main__":
    print(lijst_wortels([2.0,3.0]))