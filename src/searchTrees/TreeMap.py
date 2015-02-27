#! /usr/bin/env python

import sys

sys.path.append("../trees")
from LinkedBinaryTree import  LinkedBinaryTree
sys.path.append("../MapHashtableSkiplist")
from MapBase import MapBase
class TreeMap(LinkedBinaryTree, MapBase ):
    """
    Sorted map implementation using a binary search tree.
    """
    #---------------------------- override Position class ----------------------------
    class Position(LinkedBinaryTree.Position):
        def key(self):
            '''
            :return: key of map's key - value pair
            '''
            return self.element()._key

        def value(self):
            '''
            :return: value of  map's key - value pair.
            '''
            return self.element()._value

    #------------------------------- nonpublic utilities -------------------------------

    def _subtree_search(self, p, k):
        """
        Return Position of P's subtree having key k , or last node searched.
        :param p:
        :param k:
        :return:
        """
        if k == p.key():
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p

    def _subtree_first_position(self, p):
        """
        Return Position of first item in subtree rooted at p.
        :param p:
        :return:
        """
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        """
        Return Position of last item in subtree rooted at p.
        :param p:
        :return:
        """
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk

    def _rebalance_insert(self, p):
        pass

    def _rebalance_delete(self, p):
        pass

    def _rebalace_access(self, p):
        pass 
    #------------------------------- public utilities -------------------------------

    def first(self):
        """
        Return the first Position in the tree (or None if empty)
        :return:
        """
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        """
        Return the last Position in the tree (or None inf empty).
        :return:
        """
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def  before(self, p):
        """
        Return the Position just before p in the natural order.
        Return None if p is the first position.
        :param p:
        :return:
        """
        self._validata(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self, p):
        """
        Return the Position just after p in the natural order.
        Return None if p is the last position.
        :param p:
        :return:
        """
        self._validata(p)
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None  and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above

    def find_position(self, k):
        """
        Return position with key k, or else  neightbor (or None if empty)
        :param k:
        :return:
        """
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            return p

    def find_min(self):
        """
        Return (k,v) pair with minimum key
        :return:
        """
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())

    def find_ge(self, k):
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if p.key() < k:
                p = self.after(p)
            return (p.key(), p.value())

    def find_range(self, start, stop):
        """
        Iterate all (key,value) pairs such that start <= key < stop.
        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        :param start:
        :param stop:
        :return:
        """
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
                while p is not None and (stop is None or p.key() < stop):
                    yield (p.key(), p.value())
                    p = self.after(p)

    def __getitem__(self, k):
        """
        Return value associated with key k (raise KeyError if not found)
        :param k:
        :return:
        """
        if self.is_empty():
            raise KeyError("Key Error: " + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            if k != p.key():
                raise KeyError("Key Error: " + repr(k))
            return p.value()

    def __setitem__(self, k, v):
        """
        Assign value v to key k, overwriting existing value if present
        :param k:
        :param v:
        :return:
        """
        if self.is_empty():
            leaf = self._add_root(self._Item(k, v))
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v
                self._rebalance_access(p)
                return
            else:
                item = self._Item(k, v)
                if p.key() < k:
                    leaf = self._add_right(p, item)
                else:
                    leaf = self._add_left(p, item)
        self.rebalance_insert(leaf)

    def __iter__(self):
        """
        Generate an iteration of all keys in the map in order.
        :return:
        """
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    def delete(self, p):
        """
        Remove the item at given Position p
        :param p:
        :return:
        """
        self._validata(p)
        if self.left(p) and self.right(p):
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())
            p = replacement
        parent = self.parent(p)
        self._delete(p)
        self._rebalace_delete(parent)

    def __delitem__(self, k):
        """
        Remove item assocaited with key k (raise KeyError if not found.)
        :param k:
        :return:
        """
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)
                return
            self.rebalance_access(p)
        raise KeyError("Key Error: " + repr(k))
