#! /usr/bin/env python
#-*- coding:utf-8 -*-

from HashMapBase import HashMapBase
from UnsortedTableMap import  UnsortedTableMap

class ChainHashMap(HashMapBase):
    """
    Hash Map implemented with separate chaining for collision resolution.
    """

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError("Key Error: " + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError("Key Error: " + repr(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key


if __name__ == "__main__":
    chm = ChainHashMap()
    chm[1] = 3
    chm[1] = 4
    chm[2] = 5
    chm["a"] = 8
    for x in chm:
        print x, chm[x]
