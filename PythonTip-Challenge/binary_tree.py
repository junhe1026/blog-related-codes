# -*- coding: utf-8 -*-

"""求二叉树的宽度，先简介思路再写代码。"""

import queue


class BinTreeNode(object):
    """A binary Tree node class"""

    def __init__(self, value=None, left_child=None, right_child=None):
        self._value = value
        self._left_child = left_child
        self._right_child = right_child

    def __str__(self):
        return 'binary_tree_node with value: %s' % self._value

    __repr__ = __str__

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, n_value):
        self._value = n_value

    @property
    def left_child(self):
        return self._left_child

    @left_child.setter
    def left_child(self, n_left):
        self._left_child = n_left

    @property
    def right_child(self):
        return self._right_child

    @right_child.setter
    def right_child(self, n_right):
        self._right_child = n_right

    def has_children(self):
        return bool(self.left_child or self.right_child)


class BinTree(object):
    """binary tree class, initialize with the root node"""
    def __init__(self, root):
        self._root = root
        self._height = None

    def __str__(self):
        return 'binary_tree with root value: %s' % self._root.value

    __repr__ = __str__

    def height(self):
        if not self._height:
            self._height = self._cal_height(self._root)
        return self._height

    def is_BST(self):
        return self._BST(self._root)

    @classmethod
    def _cal_height(cls, node):
        if not node:
            return -1
        return 1 + max(cls._cal_height(node.left_child), cls._cal_height(node.right_child))

    @classmethod
    def _BST(cls, node):
        """determine if a tree is a binary search tree"""
        if not node:
            return True
        curBST = True
        if node.left_child and node.left_child.value > node.value or node.right_child and node.right_child.value < node.value:
            curBST = False
        return curBST and cls._BST(node.left_child) and cls._BST(node.right_child)


def treeWidth(tree):
    cur_width = 1
    max_width = 0
    q = queue.Queue()
    q.put(tree)
    while not q.empty():
        n = cur_width
        for i in range(n):
            tmp = q.get()
            cur_width -= 1
            if tmp.left:
                q.put(tmp.left)
                cur_width += 1
            if tmp.right:
                q.put(tmp.right)
                cur_width += 1
        if cur_width > max_width:
            max_width = cur_width
    return max_width


def preTraverse(root):
    """前序遍历"""
    if not root:
        return
    print(root.value)
    preTraverse(root.left_child)
    preTraverse(root.right_child)


def midTraverse(root):
    """中序遍历"""
    if not root:
        return
    midTraverse(root.left_child)
    print(root.value)
    midTraverse(root.right_child)


def afterTraverse(root):
    """后序遍历"""
    if not root:
        return
    afterTraverse(root.left_child)
    afterTraverse(root.right_child)
    print(root.value)



if __name__ == '__main__':
    """
             5
            / \
           3   8
          / \  / \
         1   4 6  10
    """
    n1 = BinTreeNode(value=1)
    n4 = BinTreeNode(value=4)
    n6 = BinTreeNode(value=6)
    n10 = BinTreeNode(value=10)
    n3 = BinTreeNode(value=3, left_child=n1, right_child=n4)
    n8 = BinTreeNode(value=8, left_child=n6, right_child=n10)
    n5 = BinTreeNode(value=5, left_child=n3, right_child=n8)

    # btree = BinTree(n1)
    # print(btree.height())
    # btree = BinTree(n3)
    # print(btree.height())
    # afterTraverse(n5)
    btree = BinTree(n5)
    print('height:', btree.height())
    print('is_BST?:', btree.is_BST())



