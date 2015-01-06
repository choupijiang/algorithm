# !/usr/bin/env python
# -*- coding:utf-8 -*-
from GameEntry import GameEntry


class Scoreboard:
    """
    Fixed-length sequence of high scores in nondecreasing order.
    """

    def __init__(self, capacity=10):
        """
        Initialize scoreboard with given maximum capacity.
        All entries are initially None.
        :param capacity:
        :return:
        """
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, item):
        """
        Return entry at index item
        :param item:
        :return:
        """
        return self._board[item]

    def __str__(self):
        """
        Return String representation of the high score list.
        :return:
        """
        return "\n".join(str(self._board[j]) for j in range(self._n))


    def add(self, entry):
        """
        Consider adding entry to high scores.
        :param entry:
        :return:
        """
        score = entry.get_score()
        good = self._n < len(self._board) or score > self._board[-1].get_score()
        print len(self._board)
        if good:
            if self._n < len(self._board):
                self._n += 1
            j = self._n - 1
            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j - 1]
                j -= 1
            self._board[j] = entry
        print str(sb)


if __name__ == "__main__":
    Anna = GameEntry("Anna", 660)
    Rose = GameEntry("Rose", 590)
    Paul = GameEntry("Paul", 720)
    Jack = GameEntry("Jack", 510)
    Rob = GameEntry("Rob", 750)
    Mike = GameEntry("Mike", 1105)
    sb = Scoreboard()
    sb.add(Anna)
    sb.add(Rose)
    sb.add(Paul)
    sb.add(Jack)
    sb.add(Rob)
    sb.add(Mike)