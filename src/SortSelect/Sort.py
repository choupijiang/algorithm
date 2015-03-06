#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.path.append("../linkedList")
from LinkedQueue import LinkedQueue

# ------------------Array-Based Implementation of Merge-Sort----------------------
# def merge(S1, S2, S):
# """
# Merge two sorted Python lists S1 and S2 into properly sized list S.
#     :param S1:
#     :param S2:
#     :param S:
#     :return:
#     """
#     i = j = 0
#     while i + j < len(S):
#         if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
#             S[i + j] = S1[i]
#             i += 1
#         else:
#             S[i + j] = S2[j]
#             j += 1
#
#
# def merge_sort(S):
#     """
#     Sort the elements of Python list S using the merge-sort algorithm.
#     :param S:
#     :return:
#     """
#     n = len(S)
#     if n < 2:
#         return
#     mid = n // 2
#     S1 = S[0:mid]
#     S2 = S[mid:n]
#     merge_sort(S1)
#     merge_sort(S2)
#     merge(S1, S2, S)

# ------------------queue Implementation of Merge-Sort----------------------

def merge(S1, S2, S):
    """
    Merge two sorted queue instances S1 and S2 into empty queue S.
    :param S1:
    :param S2:
    :param S:
    :return:
    """
    while not S1.is_empty() and not S2.is_empty():
        if S1.first() < S2.first():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue(S2.dequeue())
    while not S1.is_empty():
        S.enqueue(S1.dequeue())
    while not S2.is_empty():
        S.enqueue(S2.dequeue())


def merge_sort(S):
    """
    Sort the elements of queue S using the merge-sort algorithm
    :param S:
    :return:
    """
    n = len(S)
    if n < 2:
        return
    S1 = LinkedQueue()
    S2 = LinkedQueue()
    while len(S1) < n // 2:
        S1.enqueue(S.dequeue())
    while not S.is_empty():
        S2.enqueue(S.dequeue())
    merge_sort(S1)
    merge_sort(S2)
    merge(S1, S2, S)


#---------------------A Bottom-Up (Nonrecursive) Merge-Sort


def quick_sort(S):
    """
    Sort the elements of queue S using the quick-sort algorithm.
    :param S:
    :return:
    """
    n = len(S)
    if n < 2:
        return
    p = S.first()
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()
    while not S.is_empty():
        if S.first() < p:
            L.enqueue(S.dequeue())
        elif p < S.first():
            G.enqueue(S.dequeue())
        else:
            E.enqueue(S.dequeue())
    quick_sort(L)
    quick_sort(G)
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())


def inplace_quick_sort(S, a, b):
    """
    Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm.
    :param S:
    :param a:
    :param b:
    :return:
    """
    if a >= b: return
    pivot = S[b]
    left = a
    right = b - 1
    while left <= right:
        while left <= right and S[left] < pivot:
            left += 1
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right - 1
    S[left], S[b] = S[b], S[left]
    inplace_quick_sort(S, a, left - 1)
    inplace_quick_sort(S, left + 1, b)