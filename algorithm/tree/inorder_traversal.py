#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
二叉树的中序遍历（使用栈）：
中序遍历的顺序为**左-根-右**，具体算法为：
- 从根节点开始，先将根节点压入栈
- 然后再将其所有左子结点压入栈，取出栈顶节点，保存节点值
- 再将当前指针移到其右子节点上，若存在右子节点，则在下次循环时又可将其所有左子结点压入栈中
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorder_travarsal(root):
    res = []
    stack = []
    cur = root
    while cur is not None or len(stack) > 0:
        if cur is not None:
            stack.insert(0,cur)
            cur = cur.left
        else:
            cur = stack.pop(0)
            res.append(cur.val)
            cur = cur.right
    return res

if __name__ == "__main__":
    numlist = [1,2,3,4,5]
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(5)
    root.right = node1
    node1.left = node2
    node2.left = node3
    node2.right = node4

    print(inorder_travarsal(root))