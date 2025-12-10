"""Solves Advent of Code [2025 Day 8 (Part 1)]
I wrote this while learning about UnionFind, with the assistance of AI
I went on to create a v3 without the use of AI to make sure I understood the concepts
"""

import time
import math


def get_distance(point1, point2):
    """Get distance between 2 points in 3D space according to pythagoras theorem"""
    return math.sqrt(
            (point2[0]-point1[0])**2 
            + (point2[1]-point1[1])**2 
            + (point2[2]-point1[2])**2
        )


class UnionFind:
    """Manages graph of junctions and their connections"""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True


if __name__ == "__main__":
    # Read file, init variables
    start = time.time()
    junctions = []
    with open("2025/input8.txt","r", encoding="utf-8") as file:
        for index, line in enumerate(file):
            junctions.append({
                    "index": index,
                    "pos": tuple(map(int,line.strip().split(","))),
                })
    junction_count = len(junctions)

    # Assemble all possible connections
    possible_edges = {}
    for i in range(junction_count):
        for j in range(i+1, junction_count):
            junc1 = junctions[i]
            junc2 = junctions[j]
            distance = get_distance(junc1["pos"], junc2["pos"])
            possible_edges[(i, j)] = distance
    possible_edges = sorted(possible_edges.items(), key=lambda item: item[1])

    # Create circuit connections
    uf = UnionFind(junction_count)
    
    created_unions = 0
    for junctions, distance in possible_edges:
        uf.union(junctions[0], junctions[1])
        created_unions += 1
        if(created_unions == 1000):
            break
    
    circuits = {}
    for i in range(junction_count):
        root = uf.find(i)
        circuits.setdefault(root, 0)
        circuits[root] += 1


    
    sizes = sorted(circuits.values(), reverse=True)
    answer = sizes[0] * sizes[1] * sizes[2]
    print(answer)


