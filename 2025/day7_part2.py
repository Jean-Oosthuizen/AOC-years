"""This script solves adventOfCode [2025 Day 7 (Part 2)]"""


def laser_path(y, x):
    """This function traces laser paths recursively, counting paths"""
    if y == DATA_HEIGHT - 1:
        # Base case, where the laser ends
        return 1
    if (y, x) in calculated_branches:
        # Use the previously calculated number of laser paths coming from this splitter
        return calculated_branches[(y, x)]
    if rows[y][x] == "^":
        # Calculate laser paths from this splitter
        result = 0
        result += laser_path(y+1, x-1)
        result += laser_path(y+1, x+1)
        calculated_branches[(y, x)] = result
        return result
    # The laser passed through empty space
    return laser_path(y+1, x)


rows = []
with open("2025/input7.txt", "r", encoding="utf-8") as file:
    for line in file:
        rows.append(line.strip())

DATA_WIDTH = len(rows[0])
DATA_HEIGHT = len(rows)
calculated_branches = {}

for xpos in range(DATA_WIDTH):
    if rows[0][xpos] == "S":
        # The laser's paths start here
        output = laser_path(1, xpos)
        break

print(output)
