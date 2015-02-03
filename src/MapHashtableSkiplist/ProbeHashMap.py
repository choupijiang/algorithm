#! /usr/bin/env python
#-*- coding:utf-8 -*-

from HashMapBase import HashMapBase

class ProbeHashMap(HashMapBase):
    """
    Hash Map implemented with line probing for collision resolution.
    """

    #sentinal marks locations of previous deletions
    _AVAIL = object()

    def _is_available(self, j):
        """
        Return true if index j is available in table.
        :param j:
        :return:
        """
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """
        Return (success, index) tuple, described as follows:
        If match was found, success is True and index denotes its location.
        If no match found, success is False and index denotes first available slot.
        :param j:
        :param k:
        :return:
        """
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j
                if self._table[j] is None:
                    return (False, firstAvail)
            elif k == self._table[j]._key:
                return (True, j)
            j = (j + 1) % len(self._table)

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError("Key Error: " + repr(k))
        return self._table[s]._value

    def _bucket_delitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError("Key Error: " + repr(k))
        self._table[s] = ProbeHashMap._AVAIL

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k, v)
            self._n += 1
        else:
            self._table[s]._value = v

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key

if __name__ == "__main__":
    chm = ProbeHashMap()
    chm[1] = 3
    chm[1] = 4
    chm[2] = 5
    chm["a"] = 8
    for x in chm:
        print x, chm[x]