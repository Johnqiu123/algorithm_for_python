#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
选择排序：
每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，然后，
再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到全部待排序的数据元素排完。
"""

def select_sort(num_list):
    for i in range(len(num_list)):
        k = i # 代表最小值
        for j in range(i+1,len(num_list)):
            if num_list[k] > num_list[j]:
                k = j
        temp = num_list[i]
        num_list[i] = num_list[k]
        num_list[k] = temp
    return num_list


if __name__ == "__main__":
    num_list = [2,7,1,11,9,15]
    print(select_sort(num_list))