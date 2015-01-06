#! /use/env/bin python
#-*- coding:utf-8 -*-
import  sys
from PriorityQueueBase import PriorityQueueBase
sys.path.append("../linkedList")
from PositionalList import PositionalList

class Empty(Exception):
    pass


class UnsortedPriorityQueue(PriorityQueueBase):
    """
    A min-oriented priority queue implemented with an unsorted list.
    """

    def __init__(self):
        """
        Create an empty Priority Queue.
        :return:
        """
        self._data = PositionalList()

    def _find_min(self):
        """
        Return Position of item with minimum key.
        :return:
        """
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def min(self):
        """
        Return but do not remove (k,v) tuple with minimum key.
        :return:
        """
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def __len__(self):
        """
        Return the number of items in the priority queue.
        :return:
        """
        return len(self._data)

    def add(self, key, value):
        """
        Add a key-value pair.
        :param key:
        :param value:
        :return:
        """
        self._data.add_last(self._Item(key, value))

    def remove_min(self):
        """
        Remove and return (k,v) tuple with minimum key.
        :return:
        """
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)

if __name__ == "__main__":
    upq = UnsortedPriorityQueue()
    upq.add(1,"cn")
    upq.add(4,"usa")
    upq.add(3,"rs")
    print(len(upq))
    print(upq.min())