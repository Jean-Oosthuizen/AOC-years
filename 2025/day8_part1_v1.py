"""My first attempt at solving Advent of Code [2025 Day 8 (Part 1)]
It didn't make use of UnionFind, and takes forever to run, and returns the wrong result
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
    print(possible_edges)

    # Create circuit connections
    circuit_components = {}
    circuit_count = 0
    loop_count = 0
    completed_connections = []
    while loop_count <= 1000:
        print(loop_count)
        smallest_edge = {
                "edge_coords": None,
                "distance":float("inf")
            }
        for edge, distance in possible_edges.items():
            # Only get the smallest distance for junctions that aren't in a circuit yet
            if(distance < smallest_edge["distance"]):
                smallest_edge["edge_coords"] = edge
                smallest_edge["distance"] = distance
        del possible_edges[smallest_edge["edge_coords"]]
        completed_connections.append(smallest_edge["edge_coords"])

        if(smallest_edge["edge_coords"][0] in circuit_components):
            # One of the junctions in this found shortest connection is unconnected.
            # Connect it to the same circuit as the other junction
            circuit_components[smallest_edge["edge_coords"][1]] = circuit_components[smallest_edge["edge_coords"][0]]
        elif(smallest_edge["edge_coords"][1] in circuit_components):
            # One of the junctions in this found shortest connection is unconnected.
            # Connect it to the same circuit as the other junction
            circuit_components[smallest_edge["edge_coords"][0]] = circuit_components[smallest_edge["edge_coords"][1]]
        else:
            # Neither junction in this shortest connection is in a circuit.
            # Add both to a newly defined circuit
            circuit_components[smallest_edge["edge_coords"][0]] = circuit_count
            circuit_components[smallest_edge["edge_coords"][1]] = circuit_count
            circuit_count += 1        
        loop_count += 1

    # Evaluate the created circuits
    circuit_sizes = {}
    for junction, circuit_number in circuit_components.items():
        if(circuit_number in circuit_sizes):
            circuit_sizes[circuit_number] += 1
        else:
            circuit_sizes[circuit_number] = 1

    simple_size_array = list(circuit_sizes.values())    
    simple_size_array.sort(reverse=True)
    output = simple_size_array[0] * simple_size_array[1] * simple_size_array[2]

    print(f"Output: {output}")
    print(f"Execution time: {time.time() - start}")
