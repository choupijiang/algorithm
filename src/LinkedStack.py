# !/usr/bin/env python
# -*- coding:utf-8 -*-

class Empty(Exception):
    pass


class Node:
    """ Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'  # streamline memory usage

    def __init__(self, element, next):  # initialize node’s fields
        self._element = element  # reference to user’s element
        self._next = next  # reference to next node


class LinkedStack:
    """
    LILO stack implementation using a singly linked list for storage
    """

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty(" Stack is empty")
        return self._head._element

    def pop(self):
        if self.is_empty(self):
            raise Empty(" Stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


if __name__ == "__main__":
    ls = LinkedStack()
    print(ls.is_empty())
    ls.push("xx")
    ls.push("yy")
    print(ls.is_empty())
    print(ls.top())