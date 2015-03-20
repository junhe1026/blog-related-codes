# -*- coding: utf-8 -*-
""" unit test example """


from PythonTipChallenge import binary_tree
import unittest


class TestBinaryNode(unittest.TestCase):
    def setUp(self):
        self.node = binary_tree.BinTreeNode(value=1)

    def test_value_property(self):
        value = self.node.value
        self.assertEqual(value, 1)
        self.node.value = 2
        self.assertEqual(self.node.value, 2)


if __name__ == '__main__':
    unittest.main()


