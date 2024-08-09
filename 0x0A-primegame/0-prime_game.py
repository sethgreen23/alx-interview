#!/usr/bin/python3
""" Prime Game"""


def is_prime(n):
    """ Checks if a number given n is a prime number """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def calculate_primes(n, primes):
    """ Calculate all primes """
    max = primes[-1]
    if n > max:
        for i in range(max + 1, n + 1):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(0)


def isWinner(x, nums):
    """
    x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    """

    players = {"Maria": 0, "Ben": 0}

    primes = [0, 0, 2]

    calculate_primes(max(nums), primes)

    for round in range(x):
        sums = sum((i != 0 and i <= nums[round])
                   for i in primes[:nums[round] + 1])

        if (sums % 2):
            winner = "Maria"
        else:
            winner = "Ben"

        if winner:
            players[winner] += 1

    if players["Maria"] > players["Ben"]:
        return "Maria"
    elif players["Ben"] > players["Maria"]:
        return "Ben"

    return None
