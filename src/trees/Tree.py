# !/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
sys.path.append("../linkedList")
from  LinkedQueue import LinkedQueue

class Empty(Exception):
    pass

class Tree(object):
    """
    Abstract base class representing a tree structure.
    """
    #------------------------------- nested Position class -------------------------------
    class Position:
        """
        An abstraction representing the location of a single element.
        """
        def element(self):
            """
            Return the element stored at this Position.
            :return:
            """
            raise NotImplementedError('must be implemented by subclass.')

        def __eq__(self, other):
            """
            Return True if other Position represents the same location.
            :param other:
            :return:
            """
            raise NotImplementedError('must be implemented by subclass.')

        def __ne__(self, other):
            """
            Return True if other does not represent the same location.
            :param other:
            :return:
            """
            return not(self==other)

    # ---------- abstract methods that concrete subclass must support ----------
    def root(self):
        """
        Return Position representing the tree's root (or None if empty).
        :return:
        """
        raise NotImplementedError('must be implemented by subclass.')

    def parent(self):
        """
        Return Position representing p's parent (or None if p is root).
        :return:
        """
        raise NotImplementedError('must be implemented by subclass.')

    def num_children(self, p):
        """
        Return the number of children that Position p has
        :param p:
        :return:
        """
        raise NotImplementedError('must be implemented by subclass.')

    def children(self, p):
        """
        Generate an iteration of Positions representing p's children
        :param p:
        :return:
        """
        raise NotImplementedError('must be implemented by subclass.')

    def __len__(self):
        """
        Return the total number of elements in the tree.
        :return:
        """
        raise NotImplementedError('must be implemented by subclass.')

    # ---------- concrete methods implemented in this class ----------
    def is_root(self, p):
        """
        Return True if Position p represents the root of the tree.
        :param p:
        :return:
        """
        return  self.root() == p

    def is_leaf(self, p):
        """
        Return True if Position p does not have any children.
        :param p:
        :return:
        """
        return  self.num_children(p) == 0

    def is_empty(self):
        """
        Return True if the tree is empty.
        :return:
        """
        return len(self) == 0

    def depth(self, p):
        """
        Return the number of levels separating Position p from the root.
        O(n)
        :param p:
        :return:
        """
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        """
        Return the height of the tree.
        works, but O(nˆ2) worst-case time
        :return:
        """
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        """
        Return the height of the subtree rooted at Position p.
        time is linear in size of subtree
        O(n+Σp cp).
        :param p:
        :return:
        """
        if self.is_leaf(p):
            return 0
        else:
            return 1+max(self._height2(c) for c in self.children(p))

    def height(self, p = None):
        """
        Return the height of the subtree rooted at Position p.
        If p is None, return the height of the entire tree/
        :param p:
        :return:
        """
        if p is None:
            p = self.root()
        return self._height2(p)


    def __iter__(self):
        """
        Generate an iteration of the tree's elements.
        :return:
        """
        for p in self.positions():
            yield p.element()

    def positions(self):
        """
        Generate an iteration of the tree's positions.
        :return:
        """
        return self.preorder() ## alse postorder,breadthfirst

    #-----------------------Preorder Traversal-------------------------------

    def _subtree_preorder(self, p):
        """
        Generate a preorder iteration of position in subtree rooted at p.
        :param p:
        :return:
        """
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def preorder(self):
        """
        Generate a preorder iteration of positions in the tree.
        :return:
        """
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p


    #-----------------------Postorder Traversal-------------------------------

    def _subtree_postorder(self, p):
        """
        Generate a postorder iteration of positions in subtree rooted at p .
        :param p:
        :return:
        """
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def postorder(self):
        """
        Generate a postorder iteration of positions in the tree.
        :return:
        """
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    #--------------------Breadth-First Traversal-------------------------------
    def breadthfirst(self):
        """
        Generate a breadth-first iteration of the positions of the tree.
        :return:
        """
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)


