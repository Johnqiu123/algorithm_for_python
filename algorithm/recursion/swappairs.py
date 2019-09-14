#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
LeetCode 第 24号问题：两两交换链表中的节点
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 终止条件
        if head == None or head.next == None:
            return head

        # 本级递归
        next = head.next
        head.next = self.swapPairs(next.next)
        next.next = head

        # 返回值：已排好序的列表
        return next