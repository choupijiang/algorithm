#! /usr/bin/env python
#-*- coding:utf-8 -*-

from MapBase import MapBase

class SortedTableMap(MapBase):
    """
    Map implementation using a sorted table.
    """

    #----------------------------- nonpublic behaviors -----------------------------
    def _find_index(self, k, low, high):
        """
        Return index of the leftmost item with key greater than or equal to k.
        Return hight + 1 if no such item qualifies.

        That is , j will be returned such that:
            all items of slice table [low:j] have key < k
            all item of slice table [j:high] having key >= k
        :param k:
        :param low:
        :param high:
        :return:
        """

        if high < low:
            return high + 1
        else:
            mid = (low + high) / 2
            if k == self._table[mid]._key:
                return mid
            elif k < self._table[mid]._key:
                return self._find_index(k, low, mid - 1)
            else:
                return self._find_index(k, mid + 1,high)

    #----------------------------- public behaviors -----------------------------

    def __init__(self):
        """
        Create an empty map.
        :return:
        """
        self._table = []

    def __len__(self):
        """
        Return number of items in the map.
        :return:
        """
        return len(self._table)

    def __getitem__(self, k):
        """
        Return value associated with key k (raise KeyError if not found.)
        :param k:
        :return:
        """
        j = self._find_index(k, 0 , len(self._table) - 1)
