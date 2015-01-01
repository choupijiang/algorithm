# !/usr/bin/env python
# -*- coding:utf-8 -*-
from BinaryTree import BinaryTree

class LinkedBinaryTree(BinaryTree):
    """
    Linked representation of a binary tree structure.
    """

    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Postition(BinaryTree.Position):
        """
        An abstraction representing the location of a sigle element.
        """
        def __init__(self, container, node):
            """
            Constructor should not be invoked by user.
            :param container:
            :param node:
            :return:
            """
            self._container = container
            self._node = node

        def element(self):
            """
            Return the element stored at this Position.
            :return:
            """
            return self._node._element

        def __eq__(self, other):
            """
            Return True if other is a Position representing the same position.
            :param other:
            :return:
            """
            return type(other) is type(self) and other._node is self._node

    def _validata(self, p):
        """
        Return associated node , if position is valid .
        :param p:
        :return:
        """
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type.")
        if p._container is not self:
            raise ValueError("p does not belong to this container.")
        if p._node._parent is p._node:
            raise ValueError("p is no longer valid.")
        return p._node

    def _make_position(self, node):
        """
        Return Position instance for given node (or Node if no node).
        :param node:
        :return:
        """
        return  self.Position(self, node) if node is not None else None

    #-------------------------- binary tree constructor --------------------------

    def __init__(self):
        """
        Create an initially empty binary tree.
        :return:
        """
        self._root = None
        self._size = 0

    #-------------------------- public accessors --------------------------
    def __len__(self):
        """
        Return the total number of element in the tree.
        :return:
        """
        return self._size

    def root(self):
        """
        Return the root Position of the tree(or None if tree is empty.)
        :return:
        """
        return self._make_position(self._root)

    def parent(self, p):
        """
        Return the Position of p's parent(or None if p is root.)
        :param p:
        :return:
        """
        node = self._validata(p)
        return self._make_position(node._parent)

    def right(self, p):
        """
        Return the Position of p's right child(or None if no right child.)
        :param p:
        :return:
        """
        node = self._validata(p)
        return self._make_position(node._right)

    def left(self, p):
        """
        Return the Position of p's left child(or None if no left child.)
        :param p:
        :return:
        """
        node = self._validata(p)
        return self._make_position(node._left)

    def num_children(self, p):
        """
        Return the number of children of Position p.
        :param p:
        :return:
        """
        node = self._validata(p)
        count = 0
        if node._left is not None:
            count+=1
        if node._right is not None:
            count+=1
        return count




