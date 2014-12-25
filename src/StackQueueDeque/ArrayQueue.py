# !/usr/bin/env python
# -*- coding:utf-8 -*-

class Empty(Exception):
    pass

class ArrayQueue(object):
    """
    FIFO queue implementation using a Python list as underlying storage.
    """
    DEFAULT_CAPACITY = 10
    def __init__(self):
        """
        Create an empty queue.
        :return:
        """
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """
        Return the number of elements in the queue.
        :return:
        """
        return self._size

    def is_empty(self):
        """
        Return true if the queue is empty
        :return:
        """
        return self._size == 0

    def first(self):
        """
        Return (but not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        :return:
        """
        if self.is_empty():
            raise Empty("Queue is Empty")
        return self._data[self._front]

    def dequeue(self):
        """
        Remove and return the first element of the queue (i.e., FIFO)
        :return:
        """
        if self.is_empty():
            raise Empty("Queue is Empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def _resize(self,cap):
        """
        Resize to a new list of capcity >= len(self).
        :param cap:
        :return:
        """
        old = self._data
        self._data = [None]*cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0


    def enqueue(self, e):
        """
        Add an element to the back of queue.
        :return:
        """
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = ( self._front + self._size ) % len(self._data) ## --perfect wrap-around.
        self._data[avail] = e
        self._size += 1


if __name__ == "__main__":
    aq = ArrayQueue()
    aq.enqueue(100)
    aq.enqueue(101)
    aq.enqueue(98)
    aq.enqueue(1)
    aq.enqueue(2)
    aq.enqueue(3)
    aq.enqueue(4)
    aq.enqueue(5)
    aq.enqueue(6)
    aq.enqueue(7)
    aq.enqueue(8)
    print(aq.first())
    print(len(aq))
    print(aq.dequeue())
    print(len(aq))
    print(aq.dequeue())
    print(aq.dequeue())



