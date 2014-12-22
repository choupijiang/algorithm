#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Empty(Exception):
    pass

class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""
    class _Node:
        """
        Lightweight, nonpublic class for storing a singly linked node
        """
        __slots__ = '_element','_next'
        def __init__(self,element,next):
            self._element = element
            self._next = next

    def __init__(self):
        """
        create an empty queue
        :return:
        """
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """
        return the number of elements in the queue
        :return:
        """
        return self._size

    def is_empty(self):
        """
        Return True if the queue is Empty
        :return:
        """
        return self._size == 0

    def first(self):
        """
        Return (but not remove) the element of the front end of the queue
        :return:
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._head._element

    def dequeue(self):
        """
        remove and return the first element of the queue.(FIFO)
        Raise Empty exception if the queue is empty
        :return:
        """
        if self.is_empty():
            raise " Queue is Empty"
        answer = self.first()
        self._size -= 1
        self._head = self._head._next
        if self.is_empty():
            self._tail = None
        return  answer


    def enqueue(self,e):
        """
        Add an Element to the back of the queue
        :return:
        """
        newest = self._Node(e,None)
        if self.is_empty():
            self._head._next  = newest
        else:
            self._tail._next = newest

        self._tail = newest
        self._size += 1
