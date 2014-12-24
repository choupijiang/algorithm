# !/usr/bin/env python
# -*- coding:utf-8 -*-

from FavoritesList import FavoritesList
from PositionalList import PositionalList


class FavoritesListMTF(FavoritesList):
    """
    List of elements ordered by move-to-front heuristic
    """

    # override the _move_up to provide move-to-front semantics
    def _move_up(self, p):
        """
        Move accessed item at Position p to front of list.
        :param p:
        :return:
        """
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))

    # override top because list is no longer sorted
    def top(self, k):
        """
        Generate sequence of top k elements in terms of access count.
        :param k:
        :return:
        """
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k.")

        temp = PositionalList()
        for item in self._data:
            temp.add_last(item)

        for j in range(k):
            #find and report next highest form temp
            ## O(kn)
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)

            yield highPos.element()._value
            temp.delete(highPos)


if __name__ == "__main__":
    fl = FavoritesListMTF()
    fl.access(12)
    fl.access(11)
    fl.access(3)
    fl.access(12)
    fl.access(4)
    print len(fl)
    print [t for t in fl.top(4)]