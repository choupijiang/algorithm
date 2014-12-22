#!/usr/bin/env python
# -*- coding:utf-8 -*-

from DoublyLinkedBase import _DoublyLinkedBase

class Empty(Exception):
    pass

class LinkedDeque(_DoublyLinkedBase):
    """
    Double-ended queue implementation based on a doubly linked list.
    """

    def first(self):
        """
        Return (But not remove )the element at the front  of the deque
        :return:
        """
        if self.is_empty():
            raise Empty("Deque is Empty.")
        return self._head._next._element

    def last(self):
        """
        Return (But not remove) the element at the back of the deque
        :return:
        """
        if self.is_empty():
            raise Empty("Deque is Empty.")
        return self._trailer._prev._element

    def insert_first(self, e):
        """
        Add an element to the front of the deque.
        :return:
        """
        self._insert_between(e,self._head,self._head._next)

    def insert_last(self, e):
        """
        Add an element to the back of the deque.
        :param e:
        :return:
        """
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """
        Remove and return the element from the front of the deque
        Raise Empty exception if the deque is empty
        :return:
        """
        if self.is_empty():
            raise "Deque is Empty."
        self._delete_node(self._head._next)

    def delete_last(self):
        """
        Remove and return the element from the back of the deque
        Raise Empty exception if the deque is empty
        :return:
        """
        if self.is_empty():
            raise "Deque is Empty."
        self._delete_node(self._trailer._prev)
