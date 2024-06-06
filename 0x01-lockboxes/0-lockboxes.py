#!/usr/bin/python3
"""Module to solve the LOckboxes problem"""


def canUnlockAll(boxes):
    """Function that determines if all the boxes can be opened"""
    if boxes is None:
        return False
    queue = [0]
    setElements = set([0])
    while queue:
        value = queue.pop(0)
        tempList = boxes[value]
        for temp in tempList:
            if temp not in setElements and temp < len(boxes):
                queue.append(temp)
                setElements.add(temp)
    return len(setElements) == len(boxes)

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
