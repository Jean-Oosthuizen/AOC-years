"""This script solves adventOfCode [2025 Day 7 (Part 2)]"""

import time
from functools import cache


@cache
def laser_path(y, x):
    """Trace laser paths recursively and count paths"""
    if y == data_height - 1:
        # Base case, where the laser ends
        return 1
    if rows[y][x] == "^":
        # Calculate laser paths from this splitter
        result = laser_path(y+1, x-1)
        result += laser_path(y+1, x+1)
        return result
    # The laser passed through empty space
    return laser_path(y+1, x)


if __name__ == "__main__":
    start_time = time.time()
    rows = []
    with open("2025/input7.txt", "r", encoding="utf-8") as file:
        for line in file:
            rows.append(line.strip())
    data_height = len(rows[0])
    data_height = len(rows)

    for start_xpos in range(data_height):
        if rows[0][start_xpos] == "S":
            # The laser's paths start here
            output = laser_path(1, start_xpos)
            break

    print(f"Timelines: {output}")
    print(f"Execution time: {time.time() - start_time}")
