#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
LeetCode 第 20 号问题：有效的括号
解决方案：
遍历整个字符串
1、左半括号直接进栈
2、右半括号分三种情况进行判断：
   1）整个栈为空，直接返回False
   2）取出栈顶元素，作为key，查找右半括号，判断是否与字符相等，不相等直接返回False
3、遍历完成后，判断栈是否为空，不为空返回False，否则返回True
"""


def is_valid_parenthese(string):
    left_par = {"{":"}","[":"]","(":")"}
    result = []
    for i in string:
        if i in left_par:
            result.append(i)
        else:
            if len(result) == 0: return False
            val = result.pop(-1)
            if i != left_par[val]: return False
    if len(result) != 0: return False
    return True


if __name__ == "__main__":
    string = "{[}]"
    print(is_valid_parenthese(string))

