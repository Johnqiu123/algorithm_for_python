#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
希尔排序：
先取一个小于n的整数d1作为第一个增量，把数据的全部记录分组。所有距离为d1的倍数的记录放在同一个组中。
先在各组内进行直接插入排序；然后，取第二个增量d2<d1重复上述的分组和排序，直至所取的增量${d_t=1(d_t<d_t-1<...<d_2<d_1)}$，
即所有记录放在同一组中进行直接插入排序为止。
"""
def shell_sort(datalist):
    n = len(datalist)
    h = 1 # h变量保存可变增量
    while h <= n / 3:
        h = h * 3 + 1
    while h > 0:
        for i in range(h,n):
            tmp = datalist[i] # 当整体后移时，保证data[i]的值不会丢失
            # i索引处的值已经比前面所有值都大，表明已经有序，无需插入
            # i - 1索引之前的数据已经有序的，i - 1索引出元素的值就是最大值
            j = i
            while j >= h and datalist[j - h] > tmp:
                datalist[j] = datalist[j - h] # 交换
                j -= h
            datalist[j] = tmp
        h = int((h - 1) / 3)
    return datalist


if __name__ == "__main__":
    num_list = [2,7,1,11,9,15]
    print(shell_sort(num_list))

