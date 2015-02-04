#! /usr/bin/env python
#-*- coding:utf-8 -*-

class MutableMapping:
    """

    """
    def __getitem__(self, item):
        """
        Return the value associated with the key item in the MutableMapping.
        :param item:
        :return:
        """
        raise NotImplementedError("must be implemented by subclass.")

    def __setitem__(self, key, value):
        """
        Associate value   with key in map.
        :param key:
        :param value:
        :return:
        """
        raise NotImplementedError("must be implemented by subclass.")

    def __delitem__(self, key):
        """
        Romove from map with key equal key.
        if M has no such item, then raise a KeyError.
        :param key:
        :return:
        """
        raise NotImplementedError("must be implemented by subclass.")

    def __len__(self):
        """
        Return the number of items in the map.
        :return:
        """
        raise NotImplementedError("must be implemented by subclass.")

    def __iter__(self):
        """
        The default iteration for a map generates a sequence of keys in the map.
        :return:
        """
        raise NotImplementedError("must be implemented by subclass.")

    def __contains__(self, item):
        """
        Return True if the map contains an item with key item.
        :param item:
        :return:
        """
        try:
            self[item]
            return True
        except KeyError:
            return False

    def get(self, k, d=None):
        """
        Return M[k] if key k exists in the map; otherwise return  default value d.
        This provides a form to query M[k] without risk of a KeyError.
        :param d:
        :return:
        """
        try:
            return self[k]
        except KeyError:
            return d

    def setdefault(self, k, d):
        """
        If key k exists in the map, simply return M[k];
        if key k does not exist, set M[k] = d and return that value.
        :param k:
        :param d:
        :return:
        """
        try:
            return self[k]
        except KeyError:
            self[k] = d
            return d

    def pop(self, k, d=None):
        """
        Remove the item associated with key k from the map and  return its associated value v.
        If key k is not in the map,  return default value d (or raise KeyError if parameter d is
        None).
        :param k:
        :param d:
        :return:
        """
        try:
            val = self[k]
            del self[k]
            return val
        except KeyError:
            return d

    # def popitem(self):
    #     """
    #     Remove an arbitrary key-value pair from the map, and return
    #     a (k,v) tuple representing the removed pair. If map is
    #     empty, raise a KeyError.
    #     :return:
    #     """
    #     try:
    #         val = self[k]
    #         del self[k]
    #         return val
    #     except KeyError:
    #         raise KeyError("popitem(): dictionary is empty")

    def clear(self):
        """
        Remove all key-value pairs from the map.
        :return:
        """
        for key in iter(self):
            del self[key]

    def keys(self):
        """
        Return a set-like view of all keys of M.
        :return:
        """
        keys = []
        for key in iter(self):
            keys.append(key)
        return keys

    def values(self):
        """
        Return a set-like view of all values of M.
        :return:
        """
        values = []
        for key in iter(self):
            values.append(self[key])
        return values

    def items(self):
        """
        Return a set-like view of (k,v) tuples for all entries of M.
        :return:
        """
        kvs = []
        for key in iter(self):
            kvs.append((key, self[key]))
        return kvs

    def update(self, M2):
        """
        Assign M[k] = v for every (k,v) pair in map M2.
        :param M2:
        :return:
        """
        for k2 in iter(M2):
            self[k2] = M2[k2]

    def __eq__(self, M2):
        """
        Return True if maps M and M2 have identical key-value associations
        :param M2:
        :return:
        """
        if len(self) == len(M2):
            for k1 in iter(self):
                if self[k1] !=  M2[k1]:
                    return False
            return True
        return False

    def __ne__(self, M2):
        """
        Return True if maps M and M2 do not have identical keyvalue associations
        :param other:
        :return:
        """
        return not self == M2