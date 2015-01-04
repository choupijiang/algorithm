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

    def _add_root(self, e):
        """
        Place element e at the root of an empty tree and return new Postition.
        Raise ValueError if tree nonempty.
        :param e:
        :return:
        """
        if self._root is not None:
            raise ValueError("Root exists.")
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """
        Place element e at the root of an empty tree and return new Position.
        Raise ValueError if tree nonempty.
        :param p:
        :param e:
        :return:
        """
        node = self._validata(p)
        if node._left  is not None:
            raise ValueError("Left child exists.")
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """
        Create a new right child for Position p, storing element e.
        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child.
        :param p:
        :param e:
        :return:
        """
        node = self._validata(p)
        if node._right is not None:
            raise ValueError("Right child exists")
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        """
        Replace the element at position p with e, and return old element.
        :param p:
        :param e:
        :return:
        """
        node = self._validata(p)
        old =node._element
        node._element = e
        return old

    def _delete(self, p):
        """
        Delete the node at Position p, and replace it with its child, if any.
        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        :param p:
        :return:
        """
        node = self._validata(p)
        if self.num_children(p) == 2:
            raise ValueError("p has two children.")
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self.root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        """
        Attach trees t1 and t2 as left and right subtrees of external p.
        :param p:
        :param t1:
        :param t2:
        :return:
        """
        node = self._validata(p)
        if not self.is_leaf(p):
            raise ValueError("Position must be leaf.")
        if not type(self) is type(t1) is type(t2):
            raise TypeError("Tree types must match.")
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0



