# -*- coding: utf-8 -*-
import random


def bubble_sort(l):
    """
    :param l - a list
    :return a sorted list
    """
    for i in range(len(l)-1, -1, -1):
        for j in range(0, i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


def selection_sort(l):
    """
    :param l - a list
    :return a sorted list
    """
    for i in range(len(l)):
        min_index = i
        for j in range(i, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]

    return l


def insertion_sort(l):
    """
    :param l - a list
    :return a sorted list
    """
    for i in range(1, len(l)):
        tmp = l[i]
        pos = i
        for j in range(i-1, -1, -1):
            if l[j] > tmp:
                l[j+1] = l[j]
                pos = j
        l[pos] = tmp
    return l


def quick_sort(l):
    """
    :param l - a list
    :return a sorted list
    """
    if len(l) <= 1:
        return l
    else:
        pivot = l[random.randint(0, len(l)-1)]
        l_left = [i for i in l if i < pivot]
        l_right = [i for i in l if i > pivot]
        return quick_sort(l_left)+[pivot]+quick_sort(l_right)


def merge_sort(l):
    """
    :param l - a list
    :return a sorted list
    """
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    return merge(left, right)


def merge(left, right):
    i = 0
    j = 0
    result = []
    while i < len(left) or j < len(right):
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif i == len(left):
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    return result

# class quick_sort(object):
#     """移动单指针"""
#     def _partition(self, alist, p, r):
#         i = p-1
#         x = alist[r]
#         for j in range(p, r):
#             if alist[j] <= x:
#                 # 从左往右遍历，把比pivot小的，从左往右放
#                 i += 1
#                 alist[i], alist[j] = alist[j], alist[i]
#         # 把pivot放到所有小的数的最右边
#         alist[i+1], alist[r] = alist[r], alist[i+1]
#         return i+1
#
#     def _quicksort(self, alist, p, r):
#         if p < r:
#             q = self._partition(alist, p, r)
#             self._quicksort(alist, p, q-1)
#             self._quicksort(alist, q+1, r)
#
#     def __call__(self, sort_list):
#         self._quicksort(sort_list, 0, len(sort_list)-1)
#         return sort_list


if __name__ == '__main__':
    l = [95, 45, 15, 78, 84, 51, 24, 12]
    print(bubble_sort(l))
    # print(selection_sort(l))
    # print(quick_sort(l))
    # print(insertion_sort(l))
    # print(merge_sort(l))
    # a = quick_sort()
    # r = a(l)
    # print(r)
