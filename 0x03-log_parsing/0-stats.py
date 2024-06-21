#!/usr/bin/python3
"""module to read stats"""
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
# Check if the line matches the pattern
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
                print("File size: {}".format(file_size_cumulative))
                for status in status_code_list:
                    value = status_count[status]
                    if value != 0:
                        print("{}: {}".format(status, status_count[status]))
        else:
            continue
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(file_size_cumulative))
    for status in status_code_list:
        print("{}: {}".format(status, status_count[status]))
