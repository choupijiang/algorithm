#!/usr/bin/env python
# -*- coding:utf-8 -*-

from DoublyLinkedBase import _DoublyLinkedBase
class PositionalList(_DoublyLinkedBase):
    """
    A sequential container of elements allowing positional access.
    """
    #-------------------------- nested Position class --------------------------
    class Position:
        """
        An abstraction representing the location of a sigle element.
        """
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            """
            Return the elements stored at this Position.
            :return:
            """
            return self._node._element

        def __eq__(self, other):
            """
            Return True if other is a Position representing the same location.
            :param other:
            :return:
            """
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """
            Return True if others does not representing the same location.
            :param other:
            :return:
            """
            return not(self == other)

    def _validate(self,p):
        """
        Return position's node ,or raise appropriate error if invalid.
        :param p:
        :return:
        """
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container.")
        if p._node._next is None or p._node._prev is None:
            raise ValueError('p is no longer valid.')
        return p._node


    def _make_position(self, node):
        """
        Return Position instance for given node (or None if sentinel).
        :param node:
        :return:
        """
        if node is self._head or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        """
        Return the first Position in the list (or None if list is empty)
        :return:
        """
        return self._make_position(self._head._next)

    def last(self):
        """
        Return the last Position in the list (or None if list is empty)
        :return:
        """
        return  self._make_position(self._trailer._prev)

    def before(self ,p):
        """
        Return the Position just before Position p(or None if p is first).
        :param p:
        :return:
        """
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """
        Return the Position just after Position p (or None if p is last).
        :return:
        """
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """
        Generate a forward iteration of the elements of the list.
        :return:
        """
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)


    def _insert_between(self, e, prodecessor, successor):
        """
        Add element between existing nodes and return new Position
        :param e:
        :param prodecessor:
        :param successor:
        :return:
        """
        node = super(PositionalList, self)._insert_between(e, prodecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """
        Insert element e at the front of the list and return new Position.
        :param e:
        :return:
        """
        return self._insert_between(e, self._head,self._head._next)

    def add_last(self, e):
        """
        Insert element e at the back of the list and return new Postion
        :param e:
        :return:
        """
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """
        Insert element e into list before Postiion p and return new Position
        :param p:
        :param e:
        :return:
        """
        original = self._validate(p)
        return self._insert_between(e, original._prev ,original)

    def add_after(self, p ,e):
        """
        Insert element e into list after Position p and return new Position.
        :param p:
        :param e:
        :return:
        """
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """
        Remove and return the element at Position p
        :param p:
        :return:
        """
        original = self._validate(p)
        return self._delete_node(original)


    def replace(self, p, e):
        """
        Replace the element at Position p with e.

        Return the element formerly at Position p .
        :param p:
        :param e:
        :return:
        """
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

    def insertion_sort(self):
        """
        Sort PositionList of  comparable elements into nondecresing order:
        :return:
        """
        if len(self) > 1:
            marker = self.first()
            while marker != self.last():
                pivot = self.after(marker)
                value = pivot.element()
                if value > marker.element():
                    marker = pivot
                else:
                    walk = marker
                    while walk != self.first() and self.before(walk).element() > value:
                        walk = self.before(walk)
                    self.delete(pivot)
                    self.add_before(walk, value)


if __name__ == "__main__":
    pl = PositionalList()
    pl.add_first(1)
    pl.add_first(34)
    p25 = pl.add_first(25)
    pl.add_first(35)
    pl.add_first(40)

    print([el for el in iter(pl)])
    print "the last element in list is %s" % pl.last().element()
    print "the first element in list is %s" % pl.first().element()
    print "the element before "
    print ("the element before 25 is %s") % pl.before(p25).element()
    print ("the element after 25 is %s") % pl.after(p25).element()
    print ("Delete the element %s " % pl.delete(p25))
    print([el for el in iter(pl)])
    print("now Sort the list ..")
    pl.insertion_sort()
    print([el for el in iter(pl)])