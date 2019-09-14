#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
LeetCode第111号问题：二叉树的最小深度
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        if left_depth > 0 and right_depth > 0:
            return min(left_depth,right_depth) + 1
        else:
            return 1 + left_depth + right_depth