# !/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from  time import time

def sizeTest(n):
    data = []
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print("Length:{0:3d};Size in bytes:{1:4d}".format(a,b))
        data.append(None)


def compute_averate(n):
    """
    Perform n appends to an empty list and return average time elapsed.
    :param n:
    :return:
    """
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end-start)/(n+0.0)


if __name__ == "__main__":
    print("Average running time for {0:9d} is {1:.4f}".format(100,compute_averate(100)))
    print("Average running time for {0:9d} is {1:.4f}".format(1000,compute_averate(1000)))
    print("Average running time for {0:9d} is {1:.4f}".format(1000,compute_averate(1000)))
    print("Average running time for {0:9d} is {1:.4f}".format(10000,compute_averate(10000)))
    print("Average running time for {0:9d} is {1:.4f}".format(100000,compute_averate(100000)))
    print("Average running time for {0:9d} is {1:.4f}".format(1000000,compute_averate(1000000)))
    print("Average running time for {0:9d} is {1:.4f}".format(10000000,compute_averate(10000000)))

