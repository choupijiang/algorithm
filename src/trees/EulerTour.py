# !/usr/bin/env python
# -*- coding:utf-8 -*-

class EulerTour:
    """
    Abstract base class for performing Euler tour of a tree.
    """
    def __init__(self, tree):
        """
        Prepare an Euler tour template for given tree.
        :param tree:
        :return:
        """
        self._tree = tree

    def tree(self):
        """
        Return reference to the tree being traversed.
        :return:
        """
        return self._tree

    def _hook_previsit(self, p, d, path):
        pass

    def _hook_postvisit(self, p, d, path, results):
        pass

    def _tour(self, p, d, path):
        """
        Perform tour of subtree rooted at Position p.
        :param p: Position of current node being visited
        :param d: depth of p in the tree
        :param path: list of indices of children on path from root to p.
        :return:
        """
        self._hook_previsit(p, d, path)
        results = []
        path.append(0)
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path))
            path[-1] += 1
        path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def execute(self):
        """
        Perform the tour and return any result from post visit of root.
        :return:
        """
        if len(self._tree)>0:
            return self._tour(self._tree.root(), 0, [])

