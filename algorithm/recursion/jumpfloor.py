#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:

    def jump_floor(self, n):
        """存在大量的重复计算"""
        if n <= 2: return n
        else:
            return self.jump_floor(n-1) + self.jump_floor(n-2)

    def jump_floor2(self, n):
        vals = [1,1]
        while len(vals) <= n:
            vals.append(vals[-1] + vals[-2])
        return vals[n]


    def jump_more_floor(self, n):
        if n <= 1: return n
        else:
            i, tmp = 1, 1
            while i < n:
                result = 2 * tmp
                tmp = result
                i += 1
            return result


    def jump_more_floor2(self, n):
        return  1<<(n-1)


if __name__ == "__main__":
    n = 10
    s = Solution()
    print(s.jump_floor2(n))
    print(s.jump_more_floor(n))
    print(s.jump_more_floor2(n))