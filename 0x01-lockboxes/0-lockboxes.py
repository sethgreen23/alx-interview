#!/usr/bin/python3
"""Module to solve the LOckboxes problem"""


def canUnlockAll(boxes):
    """Function that determines if all the boxes can be opened"""
    if boxes is None:
        return False
    if len(boxes) == 0:
        return False
    queue = [0]
    setElements = set()
    while True:
        value = queue.pop(0)
        tempList = boxes[value]
        if value not in setElements and value < len(boxes):
            setElements.add(value)
        for temp in tempList:
            if temp not in setElements:
                queue.append(temp)
        if len(queue) == 0:
            break
    if len(setElements) == len(boxes):
        return True
    return False

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
