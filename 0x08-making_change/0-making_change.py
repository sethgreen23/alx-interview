#!/usr/bin/python3
"""
Main file for testing
"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    dp = [total + 1] * (total + 1)
    dp[0] = 0
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[total] if dp[total] < total else -1
# def makeChange(coins, total):
#     if total <= 0:
#         return 0
#     index = 0
#     coins_arranged = sorted(coins, reverse=True)
#     result = 0
#     while (True):
#         while (total >= coins_arranged[index]):
#             result += 1
#             total -= coins_arranged[index]
#         if (total < 0):
#             return 0
#         if total == 0:
#             return result
#         index += 1
#         if index >= len(coins_arranged):
#             return -1
