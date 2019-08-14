#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
LeetCode 第 2 号问题：两数相加
解决方案：
设置一个进位变量carry，建立一个新链表，把输入的两个链表从头往后同时处理，每两个相加，
将结果加上`carry`后的值作为一个新节点到新链表后面
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def add_two_numbers(l1, l2):
    """给定两个链表计算两个数之和"""
    p = l1
    q = l2
    r = ListNode(-1)
    result = r
    carry = 0
    while p or q or carry != 0:
        pval = p.val if p else 0
        qval = q.val if q else 0
        tmp = pval +qval+ carry
        num = tmp % 10
        carry = int(tmp / 10)

        node = ListNode(num)
        r.next = node
        r = node
        p = p.next if p else None
        q = q.next if q else None
    result = result.next
    return result

def traversal(listnode):
    r = listnode
    while r is not None:
        print(r.val)
        r = r.next

if __name__ == "__main__":
    l1 = ListNode(9)
    tmpl = l1
    for i in [1,6]:
        tmp = ListNode(i)
        tmpl.next = tmp
        tmpl = tmp
    traversal(l1)

    l2 = ListNode(0)
    tmp2 = l2
    for i in []:
        tmp = ListNode(i)
        tmp2.next = tmp
        tmp2 = tmp
    traversal(l2)

    result = add_two_numbers(l1,l2)
    traversal(result)



