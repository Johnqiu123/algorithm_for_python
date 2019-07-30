#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
快速排序：
随机找出一个数，可以随机取，也可以取固定位置，一般是取第一个或最后一个称为基准，
然后就是比基准小的在左边，比基准大的放到右边，如何放做，就是和基准进行交换，
这样交换完左边都是比基准小的，右边都是比较基准大的，这样就将一个数组分成了两个子数组，
然后再按照同样的方法把子数组再分成更小的子数组，直到不能分解为止。
"""

def quick_sort(datalist, l, r):
    i = l
    j = r
    if l < r:
        temp = datalist[l] # 以左边的第一个数做中枢轴
        while i != j:
            while j > i and datalist[j] > temp:
                j -= 1
            if i < j:
                datalist[i] = datalist[j]
                i += 1
            while i < j and datalist[i] < temp:
                i += 1
            if i < j:
                datalist[j] = datalist[i]
                j -= 1
        datalist[i] = temp
        quick_sort(datalist, l, i - 1)
        quick_sort(datalist, i+1, r)

if __name__ == "__main__":
    num_list = [2,7,1,11,9,15]
    quick_sort(num_list,0,len(num_list)-1)
    print(num_list)


