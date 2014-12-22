#!/usr/bin/env python
# -*- coding:utf-8 -*-

def binary_search(data, target, low ,high):
    '''
    Return True if target is found in indicated potion of a Python list
    :param data:
    :param target:
    :param low:
    :param high:
    :return:
    '''
    if low > high :
        return False
    else:
        mid = (low+high)//2
        if data[mid] == target:
            return True
        elif data[mid] > target:
            binary_search(data, target, low, mid-1)
        else:
            binary_search(data, target, mid+1, high)


if __name__ == "__main__" :
    data = [1, 2, 4, 10, 12, 30, 40, 100]
    target = 2
    print (binary_search(data, target, 0, len(data)-1))