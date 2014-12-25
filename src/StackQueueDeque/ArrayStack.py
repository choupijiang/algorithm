# !/usr/bin/env python
# -*- coding:utf-8 -*-

class Empty(Exception):
    pass

class ArrayStack:
    """
    LIFO Stack implementation using a Python list as underlying storage.
    """

    def __init__(self):
        """
        Create an empty stack.
        :return:
        """
        self._data = []

    def __len__(self):
        """
        Return the number of elements in the stack.
        :return:
        """
        return len(self._data)

    def is_empty(self):
        """
        Return True if the stack is empty.
        :return:
        """
        return len(self._data) == 0

    def push(self, e):
        """
        Add element e to the top of the stack.
        :param e:
        :return:
        """
        self._data.append(e)

    def top(self):
        """
        Return (but do not remove ) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        :return:
        """
        if self.is_empty():
            raise Empty("Stack is empty.")
        return self._data[-1]

    def pop(self):
        '''
        Return and Remove the element from the top of the stack.
        Raise Empty exception if the stack is empty.
        :return:
        '''
        if self.is_empty():
            raise Empty("Stack is empty.")
        return self._data.pop()


def is_matched(expr):
    """
    Return True if all delimiters are properly match;False otherwise.
    :param expr:
    :return:
    """
    lefty = '{[('
    righty = '}])'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif  c in righty:
            if S.is_empty():
                return False
            if righty.index(c) !=  lefty.index(S.pop()):
                return False
    return S.is_empty()

if __name__ == "__main__":
    print is_matched("[(3-3)*4-(3-4)*3]")