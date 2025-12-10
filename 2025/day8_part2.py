"""Solves Advent of Code [2025 Day 8 (Part 2)]"""

import time
from math import sqrt


def get_distance(point1, point2):
    """Get the distance between two junctions using pythagoras theorem"""
    return sqrt(
            (point1[0] - point2[0]) ** 2
            + (point1[1] - point2[1]) ** 2
            + (point1[2] - point2[2]) ** 2
        )


class UnionFind:
    """Manages graph of trees that can merge and connect"""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find_root(self, x):
        """Follows the chain of connections up to root, returns root node index"""
        # While the parent of x isn't x, follow chain of connection up
        while self.parent[x] != x:
            # Shifts parent pointer to grandparent for optimization
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        """Connect trees of nodes together"""
        root_of_a = self.find_root(a)
        root_of_b = self.find_root(b)

        if root_of_a == root_of_b:
            return False

        # Connect tree with less depth directly to root of tree with more depth
        # This avoids making any tree too deep
        if self.rank[root_of_a] > self.rank[root_of_b]:
            self.parent[root_of_b] = root_of_a
        elif self.rank[root_of_a] < self.rank[root_of_b]:
            self.parent[root_of_a] = root_of_b
        else:
            self.parent[root_of_b] = root_of_a
            self.rank[root_of_a] += 1
        return True


if __name__ == "__main__":

    # init
    start_time = time.time()
    with open("2025/input8.txt", "r", encoding="utf-8") as file:
        junctions = [list(map(int,line.strip().split(","))) for line in file]
    junction_count = len(junctions)

    # Calculate and sort all possible edge distances
    edges = []
    for i in range(junction_count):
        for j in range(i + 1, junction_count):
            edges.append((
                    get_distance(junctions[i], junctions[j]),
                    i,
                    j
                ))
    edges.sort()

    # Create circuits
    uf = UnionFind(junction_count)
    lonely_nodes = junction_count
    final_pair = None
    for distance, nodea, nodeb in edges:
        if uf.union(nodea, nodeb):
            lonely_nodes -= 1
            final_pair = [nodea, nodeb]
            if lonely_nodes == 1:
                break

    # Extract information from final pair
    output = junctions[final_pair[0]][0] * junctions[final_pair[1]][0]

    print(f"Answer: {output}")
    print(f"Execution time: {time.time() - start_time}")
