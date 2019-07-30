#!/usr/bin/env python
# -*- coding: utf-8 -*-

def merge_sort(datalist, start, end):
    if end > start:
        center = int((start + end) / 2) # 找到中间
        merge_sort(datalist, start, center)
        merge_sort(datalist, center+1, end)
        merge(datalist, start, center, end)

def merge(datalist, start, center, end):
    """合并两个有序数据"""
    rbegin = center + 1 # 右边数组第一位
    tmpindex = start # 临时数组索引
    newindex = start # 新数组索引
    temp = [0] * len(datalist)

    while start <= center and rbegin <= end:
        if datalist[start] < datalist[rbegin]:
            temp[tmpindex] = datalist[start]
            tmpindex += 1
            start += 1
        else:
            temp[tmpindex] = datalist[rbegin]
            tmpindex += 1
            rbegin += 1

    # 将剩余的数放入临时列表
    while rbegin <= end:
        temp[tmpindex] = datalist[rbegin]
        tmpindex += 1
        rbegin += 1
    while start <= center:
        temp[tmpindex] = datalist[start]
        tmpindex += 1
        start += 1
    while newindex <= end:
        datalist[newindex] = temp[newindex]
        newindex += 1


if __name__ == "__main__":
    num_list = [2, 7, 1, 11, 9, 15]
    merge_sort(num_list,0,len(num_list)-1)
    print(num_list)

