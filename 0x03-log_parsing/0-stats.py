#!/usr/bin/python3
"""Module to read stats"""
import re
import sys

pattern = re.compile(
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
    r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] '
    r'"GET /projects/260 HTTP/1.1" '
    r'(\d{3}) '
    r'(\d+)$'
)

file_size_cumulative = 0

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


def print_stats():
    """Print the current statistics."""
    global file_size_cumulative
    global status_code_list
    global status_count
    print("File size: {}".format(file_size_cumulative))
    for status in status_code_list:
        value = status_count[status]
        if value:
            print("{}: {}".format(status, value))


# Check if the line matches the pattern
def stats():
    """Stats function is called every 10 lines"""
    global file_size_cumulative
    global line_number
    global status_count
    global status_code_list
    global pattern
    try:
        for line in sys.stdin:
            match = pattern.match(line)
            if match:
                status_code = match.group(3)
                file_size = int(match.group(4))
                if status_code in status_count:
                    status_count[status_code] += 1
                file_size_cumulative += file_size
                line_number += 1
                if line_number % 10 == 0:
                    print_stats()
    except KeyboardInterrupt:
        pass
    finally:
        print_stats()


stats()
