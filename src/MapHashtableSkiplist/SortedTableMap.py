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
        if  j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[j]._value

    def __setitem__(self, k, v):
        """
        Assign value v to key k, overwriting existing value if present.
        :param k:
        :param v:
        :return:
        """
        j = self._find_index(k, 0, len(self._table) - 1)
        if  j < len(self._table) and  self._table[j]._key == k:
            self._table[j]._value = v
        else:
            self._table.insert(j ,self._Item(k, v))

    def __delitem__(self, k):
        """
        Remove item associated with k (raise KeyError if not found.)
        :param k:
        :return:
        """
        j = self._find_index(k, 0, len(self._table) - 1)
        if  j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        self._table.pop(j)

    def __iter__(self):
        """
        Generate keys of the map ordered from minimum to maximum.
        :return:
        """
        for item in self._table:
            yield item._key

    def __reversed__(self):
        """
        Generate keys of the map ordered from maximum to minimum
        :return:
        """
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        """
        Return (key,value) pair with minimum key (or None if empty).
        :return:
        """
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        """
        Return (key,value) pair with maximum key (or None if empty)
        :return:
        """
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None

    def find_ge(self, k):
        """
        Return (key,value) pair with least key greater than or equal to k.
        :param k:
        :return:
        """
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_lt(self, k):
        """
        Return (key,value) pair with greatest key strictly less than k.
        :param k:
        :return:
        """
        j = self._find_index(k, 0, len(self._table) - 1)
        if j > 0:
            return (self._table[j - 1]._key, self._table[j - 1]._value)
        else:
            return None

    def find_range(self, start, stop):
        """
        Iterate all (key,value) pairs such that start <= key < stop.
        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        :param start:
        :param stop:
        :return:
        """
        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0 ,len(self._table) - 1)
        while j < len(self._table) and (stop is None or self._table[j]._key < stop):
            yield (self._table[j]._key, self._table[j]._value)
            j += 1


if __name__ == "__main__":
    stm = SortedTableMap()
    stm[1] = 3
    stm[3] = 4
    stm[2] = 1
    for x in stm:
        print x, stm[x]
