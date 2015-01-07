#! /usr/bin/env python
#-*- coding:utf-8 -*-

from MapBase import MapBase

class UnsortedTableMap(MapBase):
    """
    Map implementation using an unordered list.
    """

    def __init__(self):
        """
        Create an empty map
        :return:
        """
        self._table = []

    def __getitem__(self, k):
        """
        Return value associated with key k (raise KeyError if not found.)
        :param item:
        :return:
        """
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError("Key Error: " + repr(k))

    def __setitem__(self, key, value):
        """
        Assign value v to key k,overwriting existsing value if present.
        :param key:
        :param value:
        :return:
        """
        for item in self._table:
            if key == item._key:
                item._value = value
                return
        self._table.append(self._Item(key, value))


    def __delitem__(self, key):
        """
        Remove item associated with key k (raise KeyError if not found)
        :param key:
        :return:
        """
        for j in range(len(self._table)):
            if key == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError("Key Error: " + repr(key))

    def __len__(self):
        """
        Return number of items in the map.
        :return:
        """
        return len(self._table)

    def __iter__(self):
        """
        Generate iteration of the map's keys.
        :return:
        """
        for item in self._table:
            yield item._key


if __name__ == "__main__":
    m = UnsortedTableMap()
    m["1002"] = "a"
    m["1003"] = "b"
    m["1004"] = "c"
    print(m.items())