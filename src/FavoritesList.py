#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PositionalList import  PositionalList

class FavoritesList:
    """
    List of elements ordered from most frequently accessed to least.
    """
    #------------------------------ nested Item class ------------------------------
    class _Item:
        __slots__ = '_value', '_count'
        def __init__(self, e):
            self._value = e
            self._count = 0

    #------------------------------- nonpublic utilities -------------------------------
    def _find_position(self, e):
        """
        Search for element e and return its Position (or None if not found).
        :param e:
        :return:
        """
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        """
        Move item at Position p earlier in the list based on access count.
        :param p:
        :return:
        """
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while(walk != self._data.first() and cnt > self._data.before(walk)._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))


    #------------------------------- public methods -------------------------------

    def __init__(self):
        """
        Create an empty list of favorites.
        :return:
        """
        self._data =PositionalList()

    def __len__(self):
        """
        Return number of entries on favorites list.
        :return:
        """
        return len(self._data)


    def is_empty(self):
        """
        Return True is list is empty.
        :return:
        """
        return len(self._data) == 0


    def access(self, e):
        """
        Access element e,thereby increasing its access count.
        :param e:
        :return:
        """
        p = self._find_position(e)
        if p is None:
            p = self._data.add_last(self._Item(e))
        p.element()._count += 1
        self._move_up(p)

    def remove(self, e):
        """
        Remove element e from the list of favorites
        :param e:
        :return:
        """
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)

    def top(self, k):
        """
        Generate sequence of top k elements in terms of access count.
        :param e:
        :return:
        """
        if not 1 <= len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        for j in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)

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

    fl = FavoritesList()
    fl.access("12")
    fl.access("11")
    fl.access("3")
    fl.access("12")
    fl.access("4")
    print len(fl)
    print [t for t in fl.top(4) ]