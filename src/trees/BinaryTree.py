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


    #--------------------inorder  Traversal-------------------------------
    def _subtree_inorder(self, p):
        """
        Generate an inorder iteration of positions in subtree rooted at p
        :param p:
        :return:
        """
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def inorder(self):
        """
        Generate an inorder iteration of positions in the tree.
        :return:
        """
        if not self.is_empty():
          for p in self._subtree_inorder(self.root()):
              yield p
