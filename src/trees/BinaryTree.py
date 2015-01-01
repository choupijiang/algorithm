# !/usr/bin/env python
# -*- coding:utf-8 -*-

from Tree import Tree

class BinaryTree(Tree):
    """
    Abstract base class representing a binary tree structure.
    """
    # --------------------- additional abstract methods ---------------------
    def left(self, p):
        """
        Return a Position representing p's left child.
        Return None if p does not have a left hand.
        :param p:
        :return:
        """
        raise NotImplementedError('must be implemented by subclass.')

    def right(self, p):
        """
        eturn a Position representing p's right child.
        Return None if p does not have a right hand.
        :param p:
        :return:
        """
        raise NotImplementedError('must be implemented by subclass.')

    # ---------- concrete methods implemented in this class ----------
    def sibling(self, p):
        """
        Return a Position representing p's sibling (or None if no sibling)
        :param p:
        :return:
        """
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """
        Generate an iteration of Positions representing p's children.
        :param p:
        :return:
        """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
