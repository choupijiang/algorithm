#! /usr/bin/env python
#-*- coding:utf-8 -*-


from MapBase import MapBase
from random import randrange


class HashMapBase(MapBase):
    """
    Abstract base class for map using hash-table with MAD compression.
    """
    def __init__(self, cap=11, p=109345121):
        """
        Create an empty hash-table map.
        :param cap:
        :param p:
        :return:
        """
        self._table = cap * [None]
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p - 1)
        self._shift = randrange(p)

    def _hash_function(self, k):
        """
        :param k:
        :return:
        """
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error:' + repr(k))
        return bucket[k]

