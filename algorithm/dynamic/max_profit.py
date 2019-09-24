#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
LeetCode 第 121 号问题：买卖股票的最佳时间

"""

def max_profit(prices):
    """k=1"""
    if len(prices) <= 1: return 0
    buy,sell = -prices[0] , 0
    for i in range(len(prices)):
        buy = max(buy, -prices[i])
        sell = max(sell, prices[i] + buy)
        print(buy, sell)
    return sell


def max_profit_inf(prices):
    """k=inf"""
    if len(prices) <= 1: return 0
    buy,sell = -prices[0] , 0
    for i in range(len(prices)):
        temp = sell
        sell = max(sell, prices[i] + buy)
        buy = max(buy, temp-prices[i])
        print(buy, sell)
    return sell


if __name__=="__main__":
    prices = [7,1,5,3,6,4]
    max_profit(prices)