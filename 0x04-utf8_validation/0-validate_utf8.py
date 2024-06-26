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


def get_num_bytes(byte):
    """Get the number of bytes for a character"""
    binary = num_bin(byte)
    if binary[0] == '0':
        return 1
    count = 0
    for bit in binary:
        if bit == '1':
            count += 1
        else:
            break
    return count if 1 < count <= 4 else 0


def is_continuation_byte(byte):
    """Check if a byte is a continuation byte"""
    return num_bin(byte)[:2] == '10'


def validUTF8(data):
    """Validate utf8"""
    i = 0
    while i < len(data):
        # Get the number of bytes for this character
        num_bytes = get_num_bytes(data[i])
        if num_bytes == 0:
            return False

        # Check if there are enough bytes left in data
        if i + num_bytes > len(data):
            return False

        # Validate the correct number of continuation bytes
        for j in range(i + 1, i + num_bytes):
            if not is_continuation_byte(data[j]):
                return False

        # Move i to the start of the next character
        i += num_bytes

    return True
