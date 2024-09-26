#!/usr/bin/python3
"""
Module to calculate how much rainwater is retained after it rains.
"""


def rain(walls):
    """
    Calculate how many square units of water will be retained after it rains.

    Arguments:
    walls -- list of non-negative integers representing wall heights

    Returns:
    Integer indicating total amount of rainwater retained.
    """
    water = 0
    if not walls or len(walls) < 3:
        return water

    n = len(walls)
    prev_wall = walls[0]
    next_wall = 0

    for i in range(1, n - 1):
        if walls[i] != 0:
            prev_wall = walls[i]
        else:
            if prev_wall == 0:
                continue
            else:
                for j in range(i + 1, n):
                    if walls[j] != 0:
                        next_wall = walls[j]
                        break
                if next_wall == 0:
                    continue
                water += min(prev_wall, next_wall)

    return water
