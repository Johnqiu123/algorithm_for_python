#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
冒泡排序：
比较相邻的元素。如果第一个比第二个大，就交换他们两个。对每一对相邻元素做同样的工作，
从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。针对所有的元素重复以上的步骤，
除了最后一个。持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较
"""

def bubble_sort(data_list):
    count = 1
    for i in range(len(data_list)-1):
        flag = 0
        for j in range(len(data_list)-1-i):
            print(i,count)
            count += 1
            if data_list[j] > data_list[j+1]:
                flag = 1
                data_list[j],data_list[j+1] = data_list[j+1],data_list[j]
        if flag == 0: break
    return data_list


if __name__ == "__main__":
    num_list = [2, 7, 1, 11, 9, 15]
    # num_list = [2, 7, 1, 11, 9, 15,13,16,1,2,4,6,86,5,43,12,32,20]
    print(bubble_sort(num_list))

