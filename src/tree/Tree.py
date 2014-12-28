# !/usr/bin/env python
# -*- coding:utf-8 -*-

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
        Return the
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
        :return:
        """
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        """
        Return the height of the subtree rooted at Position p.
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



