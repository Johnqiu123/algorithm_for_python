# LeetCode第111号问题：二叉树的最小深度

### 题目描述

题目链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

**说明:** 叶子节点是指没有子节点的节点。

**示例:**

给定二叉树 `[3,9,20,null,null,15,7]`

```
    3
   / \
  9  20
    /  \
   15   7

```

返回它的最小深度  2.

### 题目解析

使用递归来做。套用递归解题三部曲模板：

1. **找终止条件**。当树为空时，树的深度为0，递归结束
2. **找返回值**。返回root的左右子树的最小深度，再加上1
3. **本级递归应该做什么。** 分别获取左右子树的最小深度，然后进行比较返回，如果左右最小深度都不为空，则取两者最小值，然后+1，否则取他们的相加和

### 代码实现

Python版本实现：

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
        

```

