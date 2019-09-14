#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
LeetCode 第 104号问题：二叉树的最大深度
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 0 if root == None else max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1