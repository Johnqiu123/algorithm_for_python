#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
LeetCode 第 1 号问题：两数之和
解决方案：
使用查找表的方法解决
构建字典来存储元素的值与索引，然后遍历nums：
（1）如果目标值与当前元素的差值在字典中，直接返回差值的索引与当前值的索引
（2）否则，将当前的值与索引存入字典中
"""


def two_sum(nums, target):
    num_dict = {}
    for i in range(len(nums)):
        if target - nums[i] in num_dict:
            return [num_dict[target-nums[i]],i]
        else:
            num_dict[nums[i]] = i  # 构建 数值：序号对


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))

