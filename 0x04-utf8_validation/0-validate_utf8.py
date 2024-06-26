#!/usr/bin/python3
"""Validate utf8"""


def num_bin(number):
    """Return the binary representation of a number"""
    # get the binary representation of the number
    binary_rep = bin(number)[2:]
    return binary_rep.zfill(8)


def get_num_bytes(byte):
    """Get the number of bytes for a character"""
    binary = num_bin(byte)

    # check if the first byte is 0
    if binary[0] == '0':
        return 1
    # count the number of bytes
    count = 0
    for bit in binary:
        if bit == '1':
            count += 1
        else:
            break
    return count if 1 < count < 5 else 0


def is_continuation_byte(byte):
    """Check if a byte is a continuation byte"""
    return num_bin(byte)[:2] == '10'


def validUTF8(data):
    """Validate utf8"""
    i = 0
    while i < len(data):
        # get the number of bytes for the current character
        num_bytes = get_num_bytes(data[i])

        if num_bytes == 0:
            return False
        # check the number of bytes if valid
        if i + num_bytes > len(data):
            return False
        for j in range(i + 1, i + num_bytes):
            if not is_continuation_byte(data[j]):
                return False
        i += num_bytes
    return True
