#!/usr/bin/python3
"""Validate utf8"""


def num_bin(number):
    """Return the binary representation of a number"""
    # get the 8significan numbers
    eight_least_char = number & 255
    # get the binary representation of the number
    binary_repr = bin(eight_least_char)[2:]
    # fill the number with 0 on the left
    return binary_repr.zfill(8)


def validUTF8(data):
    """Determine if the given data set represents a valid UTF-8 encoding."""
    least_bit_hash = {
        '0': 0,
        '10': 1,
        '110': 2,
        '1110': 3,
        '11110': 4
    }
    if len(data) == 0:
        return False
    first_character = num_bin(data[0])
    valid_first_bytes = True
    count = 1
    for b in sorted(least_bit_hash.keys()):
        if first_character[:count] != b:
            valid_first_bytes = False
        if first_character[:count] == b:
            key = b
            valid_first_bytes = True
            break
        count += 1
    if not valid_first_bytes:
        return False
    if len(data) < least_bit_hash[key]:
        return False
    for test_num in data[1:count + 1]:
        item = num_bin(test_num)
        if item[:2] != '10' or test_num == 256:
            return False
    return True
