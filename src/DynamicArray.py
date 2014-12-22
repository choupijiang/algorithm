#!/usr/bin/env python
# -*- coding:utf-8 -*-

import  ctypes

class DynamicArray:

    def __init__(self):
        self._size = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def _make_array(self,c):
        """Return new array with capacity c"""
        return (c*ctypes.py_object)()

    def __len__(self):
        return self._size

    def __getitem__(self, item):
        if not 0 <= item <= self._size:
            raise IndexError( 'invalid index ')
        return self._A[item]

    def _resize(self,c):
        B = self._make_array(c)
        for k in range(self._size):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def append(self,obj):
        if self._size == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._size] = obj
        self._size += 1

if __name__ == "__main__":
    dA = DynamicArray()
    dA.append(123)
    dA.append(90)
    dA.append(24)
    print(dA[1])