#! /usr/bin/env python
# -*- coding:utf-8 -*-

from TreeMap import TreeMap


class AVLTreeMap(TreeMap):
    """
    Sorted map implementation using an AVL tree.
    """

    # -------------------------nested _Node class-----------------------------
    class _Node(TreeMap._Node):
        """
        Node class for AVL maintains height value for balancing.
        """
        __slots__ = '_height'

        def __init__(self, element, parent=None, left=None, right=None):
            super(AVLTreeMap._Node, self).__init__(element, parent, left, right)
            self._height = 0 # will be recomputed during balancing

        def left_height(self):
            return self._left._height if self._left is not None else 0

        def right_height(self):
            return self._right._height if self._right is not None else 0


    #------------------------- positional-based utility methods -------------------------
    def _recompute_height(self, p):
        p._node._height = 1 + max(p._node.left_height(), p._node.right_height())

    def _isbalance(self, p):
        return abs(p._node.left_height() - p._node.right_height())<=1

    def _tall_child(self, p, favorleft=False):
        if p._node.left_height() + (1 if favorleft else 0) > p._node.right_height():
            return self.left(p)
        else:
            return self.right(p)

    def _tall_grandchild(self, p):
        child = self._tall_child(p)
        # if child is on left, favor left grandchild; else favor right grandchild
        alignment = (child == self.left(p))
        return self._tall_child(child, alignment)

    def _rebalace(self, p):
        while p is not None:
            old_height = p._node._height
            if not self._isbalance(p):
                p = self._restructure(self._tall_grandchild(p))
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
            self._recompute_height(p)
            if p._node._height == old_height:
                p = None
            else:
                p = self.parent(p)

    #---------------------------- override balancing hooks ----------------------------
    def _rebalance_insert(self, p):
        self._rebalace(p)

    def _rebalance_delete(self, p):
        self._rebalace(p)


if __name__ == "__main__":
    avlTree = AVLTreeMap()
    avlTree[3] = 3
    avlTree[1] = 1
    avlTree[4] = 4
    avlTree[6] = 6
    avlTree[2] = 2
    avlTree[5] = 5
    print (avlTree.preorder_label(avlTree.root(),0,[]))
    print(avlTree.parenthesize(avlTree.root()))
    for k in iter(avlTree):
        print k,avlTree[k]
