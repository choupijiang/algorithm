# !/usr/bin/env python
# -*- coding:utf-8 -*-

class _DoublyLinkedBase(object):
    """
    A base class providing a doubly linked list representation.
    """

    class _Node:
        """
        Lightweight, nonpublic class for storing a doubly linked node.
        """
        __slots__ = '_element', '_prev', "_next"

        def __init__(self, element, prev, next):
            self._element = element
            self._next = next
            self._prev = prev

    def __init__(self):
        """
        create an empty list.
        :return:
        """
        self._head = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._head._next = self._trailer
        self._trailer._prev = self._head
        self._size = 0

    def __len__(self):
        """
        return the number of elements in the link list
        :return:
        """
        return self._size

    def is_empty(self):
        """
        Return True if list is empty
        :return:
        """
        return self._size == 0

    def _insert_between(self, e, prodecessor, successor):
        """
        add element e between two existing nodes and return new node .
        :param e:
        :param prodecessor:
        :param successor:
        :return:
        """
        newest = self._Node(e, prodecessor, successor)
        prodecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest


    def _delete_node(self, node):
        """
        Delete nonsentinel node from the list and return its element
        :param node:
        :return:
        """
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element
