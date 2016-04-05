# !/usr/bin/env python
# -*- coding:utf-8 -*-

def insertion_sort(A):
    """
    Sort list of comparable elements into nondecreasing order.
    :param A:
    :return:
    """
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j - 1] > cur:
            A[j] = A[j - 1]
            j -= 1
        A[j] = cur



if __name__ == "__main__":
    a = [3, 12, 10, 4, 6]
    insertion_sort(a)
    print a