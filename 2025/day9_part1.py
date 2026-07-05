"""Solves Advent of Code [2025 Day 9 (Part 1)]"""

import time


def get_area(tile_1, tile_2):
    """Find the rectangular area of a grid, inclusive of the row/column of cells provided"""
    return abs((tile_1[0] - tile_2[0] + 1) * (tile_1[1] - tile_2[1] + 1))


if __name__ == "__main__":
    start = time.time()

    with open("2025/input9.txt", "r", encoding="utf-8") as file:
        red_tiles = [list(map(int, line.split(","))) for line in file]

    largest_area = -1
    red_tile_count = len(red_tiles)
    for i in range(red_tile_count):
        for j in range(i+1, red_tile_count):
            area = get_area(red_tiles[i], red_tiles[j])
            print(area)
            largest_area = max(largest_area, area)

    print(f"Answer: {largest_area}")
    print(f"Execution time: {time.time() - start}")
