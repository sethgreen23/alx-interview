#!/usr/bin/python3
"""
Minimum Operations"""


def minOperations(n):
    """Minimum Operations"""
    if n < 2:
        return 0
    countOperation = 0
    factor = 2
    while n > 1:
        if n % factor != 0:
            factor += 1
            continue
        countOperation += factor
        n = n // factor
    return countOperation
