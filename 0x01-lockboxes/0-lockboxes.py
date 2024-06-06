#!/usr/bin/python3
"""Module to solve the LOckboxes problem"""


def canUnlockAll(boxes):
    """Function that determines if all the boxes can be opened"""
    if not boxes:
        return False

    n = len(boxes)
    queue = [0]
    unlocked = set([0])

    while queue:
        box_index = queue.pop(0)
        for key in boxes[box_index]:
            if 0 <= key < n and key not in unlocked:
                unlocked.add(key)
                queue.append(key)

    return len(unlocked) == n


# def canUnlockAll(boxes):
#     """Function that determines if all the boxes can be opened"""
#     if boxes is None:
#         return False
#     if len(boxes) == 0:
#         return False
#     keys = [0]
#     for key in keys:
#         if key >= len(boxes) or boxes[key] is None:
#             continue
#         for i in boxes[key]:
#             if i not in keys and i < len(boxes):
#                 keys.append(i)
#     return len(keys) == len(boxes)
