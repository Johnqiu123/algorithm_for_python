#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
插入排序：
首先将数组分成有序和无序部分（左边第一个数字默认为有序），然后不断将右边的无序部分的数字插入左边，
如果在它的左边的数字比它大，进行交换，这个动作一直继续下去，直到这个数字的左边数字比它还要小，
就可以停止了。然后完成排序
"""

def insert_sort(num_list):
    for i in range(1, len(num_list)):
        temp = num_list[i]
        j = i - 1
        while j >= 0 and temp < num_list[j]:
            num_list[j + 1] = num_list[j]
            j -= 1
        num_list[j+1] = temp
    return num_list


if __name__ == "__main__":
    num_list = [2,7,1,11,9,15]
    print(insert_sort(num_list))