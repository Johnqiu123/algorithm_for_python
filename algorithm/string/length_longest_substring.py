#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
LeetCode 第 3 号问题：无重复字符的最长子串
维护一个滑动窗口，窗口内的都是没有重复的字符，去尽可能的扩大窗口的大小，窗口不停的向右滑动。
（1）如果当前遍历到的字符从未出现过，那么直接扩大右边界；
（2）如果当前遍历到的字符出现过，则缩小窗口（左边索引向右移动），然后继续观察当前遍历到的字符；
（3）重复（1）（2），直到左边索引无法再移动；
（4）维护一个结果res，每次用出现过的窗口大小来更新结果 res，最后返回 res 获取结果
"""
import time

def length_of_longest_substring(string):
    nowlist = []
    right,left = -1,0
    res = 0
    while left < len(string):
        if right + 1 < len(string) and string[right+1] not in nowlist:
            right += 1
            nowlist.append(string[right])
        else:
            nowlist.pop(0)
            left += 1
        res = max(res, right - left + 1)
    return  res

if __name__ == "__main__":
    string = "abbc"
    start = time.time()
    print(length_of_longest_substring(string))
    end = time.time()
    print(end-start)

