# !/usr/bin/env python
# -*- coding:utf-8 -*-

import ctypes


class DynamicArray:
    def __init__(self):
        """
        Create an empty array.
        :return:
        """
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def _make_array(self, c):
        """Return new array with capacity c"""
        return (c * ctypes.py_object)()

    def __len__(self):
        """
        Return number of elements stored in the array.
        :return:
        """
        return self._n

    def __getitem__(self, item):
        '''
        Rreturn element at index k.
        :param item:
        :return:
        '''
        if not 0 <= item <= self._n:
            raise IndexError('invalid index ')
        return self._A[item]

    def _resize(self, c):
        """
        Resize internal array to capacity c.
        :param c:
        :return:
        """
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def append(self, obj):
        '''
        Add object to end of the array.
        :param obj:
        :return:
        '''
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def insert(self, k, value):
        """
        Insert value at index k, shifting subsequent valus rightward.
        :param k:
        :param value:
        :return:
        """
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]
        self._A[k] = value

    def remove(self, value):
        """
        Remove first occurrence
        :param value:
        :return:
        """
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n, -1):
                    self._A[j] = self._A[j+1]
                self._A[self._n-1] = None
                self._n -= 1
                return
        raise ValueError("value not found")


if __name__ == "__main__":
    dA = DynamicArray()
    dA.append(123)
    dA.append(90)
    dA.append(24)
    print(dA[1])