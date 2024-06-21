#!/usr/bin/python3
"""module to read stats"""
import re
import sys

# Regular expression pattern with capturing groups
pattern = re.compile(
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '  # IP Address
    r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] '  # Date
    r'"GET /projects/260 HTTP/1.1" '  # Request
    r'(\d{3}) '  # Status Code
    r'(\d+)$'  # File Size
)

file_size_cumulative = 0

status_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

status_code_list = [200, 301, 400, 401, 403, 404, 405, 500]

line_number = 0
# Check if the line matches the pattern
try:
    for line in sys.stdin:
        match = pattern.match(line)
        line_number += 1
        if match:
            status_code = int(match.group(3))
            file_size = int(match.group(4))
            if status_code in status_code_list:
                status_count[status_code] += 1
            file_size_cumulative += file_size
            if line_number % 10 == 0:
                print("File size: {}".format(file_size_cumulative))
                for status in status_code_list:
                    print("{}: {}".format(status, status_count[status]))
        else:
            continue
except KeyboardInterrupt:
    print("File size: {}".format(file_size_cumulative))
    for status in status_code_list:
        print("{}: {}".format(status, status_count[status]))
