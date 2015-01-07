#! /use/env/bin python
#-*- coding:utf-8 -*-

#########################################
## adaptable heapq
#########################################

from  HeapPriorityQueue import HeapPriorityQueue

class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    """
    A location-based priority queue implemented with a binary heap.
    """
    #-----------------------nested Locator class------------------------------
    class Locator(HeapPriorityQueue._Item):
        """
        Token for locating an entry of the priority queue.
        """
        __slots__ = '_index'

        def __init__(self, k, v, j):
            super(AdaptableHeapPriorityQueue.Locator, self).__init__(k, v)
            self._index = j

    #------------------------------ nonpublic behaviors ----------------------

    def _swap(self, i, j):
        super(AdaptableHeapPriorityQueue, self)._swap(i ,j)
        self._data[i]._index = j
        self._data[j]._index = i

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self, key, value):
        """
        Add a key-value pair.
        :param key:
        :param value:
        :return:
        """
        token = self.Locator(key, value, len(self._data))
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token

    def update(self, loc, newkey, newval):
        """
        Update the keu and value for the entry identified by Location loc.
        :param loc:
        :param newkey:
        :param newval:
        :return:
        """
        j = loc._index
        if not (0 < j < len(self._data) and self._data[j] is loc):
            raise ValueError("Invalid locator.")
        loc._key = newkey
        loc._value = newval
        self._bubble(j)

    def remove(self, loc):
        """
        Remove and return the (k,v) pair identified by Location loc.
        :param loc:
        :return:
        """
        j = loc._index
        if not (0 < j < len(self._data) and self._data[j] is loc):
            raise ValueError("Invalid locator.")
        if j == len(self._data) - 1:
            self._data.pop()
        else:
            self._swap(j, len(self) - 1)
            self._data.pop()
            self._bubble(j)
        return (loc._key, loc._value)

