#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def judge_node(self, root):
        # 终止条件：该节点值为空
        if root == None:
            return (0, True)

        # 本级递归
        left_height, left_val = self.judge_node(root.left)
        right_height, right_val = self.judge_node(root.right)
        height = max(left_height, right_height) + 1
        if left_val == False or right_val == False or abs(left_height - right_height) > 1:
            return (height, False)

        # 返回值:(高度，是否是平衡二叉树)
        return (height, True)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.judge_node(root)[1]