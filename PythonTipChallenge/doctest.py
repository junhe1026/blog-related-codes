# -*- coding: utf-8 -*-

"""used to write doctest """

import doctest
from PythonTipChallenge import binary_tree

doctest.testmod(binary_tree, verbose=True)

# Trying:
#     n1 = BinTreeNode(value=1)
#     n4 = BinTreeNode(value=4)
#     n6 = BinTreeNode(value=6)
#     n10 = BinTreeNode(value=10)
#     n3 = BinTreeNode(value=3, left_child=n1, right_child=n4)
#     n8 = BinTreeNode(value=8, left_child=n6, right_child=n10)
#     n5 = BinTreeNode(value=5, left_child=n3, right_child=n8)
# Expecting nothing
# Trying:
#     n1.value
# Expecting
#     1
