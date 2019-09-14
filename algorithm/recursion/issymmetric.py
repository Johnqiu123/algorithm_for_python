#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
LeetCode 第 101号问题：对称二叉树
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def is_mirror(self, p, q):
        # 终止条件
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        # 本级递归
        if p.val == q.val:
            return self.is_mirror(p.left, q.right) and self.is_mirror(p.right, q.left)
        return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_mirror(root, root)
