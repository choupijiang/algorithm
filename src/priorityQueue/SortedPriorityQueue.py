#! /use/env/bin python
#-*- coding:utf-8 -*-
#########################################
##Sorted Priority Queue.
##Insertion-sort.
#########################################
import  sys
from PriorityQueueBase import PriorityQueueBase
sys.path.append("../linkedList")
from PositionalList import PositionalList

class Empty(Exception):
    pass


class SortedPriorityQueue(PriorityQueueBase):
    """
    A min-oriented priority queue implemented with an sorted list.
    """

    def __init__(self):
        """
        Create a new empty Priority Queue.
        :return:
        """
        self._data = PositionalList()

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
        newest = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data._add_first(newest)
        else:
            self._data.add_before(walk, newest)

    def min(self):
        """
        Return but do not remove(k,v) tuple with minimum key.
        :return:
        """
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """
        Remove and return (k,v) tuple with minimun key.
        :return:
        """
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        item = self._data.delete(self._data.first())
        return (item._key, item._value)

if __name__ == "__main__":
    spq = SortedPriorityQueue()
    spq.add(5,"cn")
    spq.add(4,"usa")
    spq.add(3,"rs")
    print(len(spq))
    print(spq.min())

