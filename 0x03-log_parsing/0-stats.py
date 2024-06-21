#!/usr/bin/python3
"""Module to read stats"""
import re
import sys

pattern = re.compile(
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
    r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] '
    r'"GET /projects/260 HTTP/1.1" '
    r'(\d{3}) '
    r'(\d+)$'
)

total_size = 0

status_count = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

status_code_list = ['200', '301', '400', '401', '403', '404', '405', '500']

line_number = 0


def print_stats(total_size: int,
                status_count: dict,
                status_code_list: list) -> None:
    """Print the current statistics."""
    print("File size: {}".format(total_size))
    for status_code in status_code_list:
        value = status_count[status_code]
        if value:
            print("{}: {}".format(status_code, value))


# Check if the line matches the pattern
def stats() -> None:
    """Stats function is called every 10 lines"""
    global total_size
    global line_number
    global status_count
    global status_code_list
    global pattern

    try:
        for line in sys.stdin:
            line_number += 1
            match = pattern.match(line)
            if not match:
                continue

            status_code = match.group(3)
            if status_code not in status_count:
                continue

            file_size = int(match.group(4))
            status_count[status_code] += 1
            total_size += file_size

            if line_number % 10 == 0:
                print_stats(total_size, status_count, status_code_list)

    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_count, status_code_list)


stats()
