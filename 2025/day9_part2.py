"""Solves Advent of Code [2025 Day 9 (Part 1)]"""

import time



def get_area(point_1, point_2):
    """Find the rectangular area of a grid, inclusive of the row/column of cells provided"""
    return abs((point_1[0] - point_2[0] + 1) * (point_1[1] - point_2[1] + 1))


def point_edge_intersect_type(point, coordinates, vertical):
    """Determine if a point lies between two coordinates - not inclusive of the coordinates"""
    
    if point in coordinates:
        return "vertex"
    
    if coordinates[0][0] < coordinates[1][0]:
        x_range = [coordinates[0][0], coordinates[1][0]]
    else:
        x_range = [coordinates[1][0], coordinates[0][0]]
    
    if coordinates[0][1] < coordinates[1][1]:
        y_range = [coordinates[0][1], coordinates[1][1]]
    else:
        y_range = [coordinates[1][1], coordinates[0][1]]
    
    # print(f"y_range: {y_range}")
    # print(f"x_range: {x_range}")
    # print(f"{x_range[0]} < {point[0]} and {point[0]} < {x_range[1]} and {y_range[0]} < {point[1]} and {point[1]} < {y_range[1]}")
    
    if (vertical):
        if (y_range[0] <= point[1] and point[1] <= y_range[1]
            and x_range[0] == point[0]):
            return "on edge"
    else:
        if (x_range[0] <= point[0] and point[0] <= x_range[1]
            and y_range[0] == point[1]):
            return "on edge"
        
    return "none"


def get_rect_edges(vertex_1, vertex_2):
    """Generate 4 edges forming a rectangle with 2 vertices as opposite corners"""
    vertex_3 = [vertex_1[0], vertex_2[1]]
    vertex_4 = [vertex_2[0], vertex_1[1]]
    return [
        Edge(vertex_1, vertex_3),
        Edge(vertex_1, vertex_4),
        Edge(vertex_2, vertex_3),
        Edge(vertex_2, vertex_4),
    ]


class Edge:
    def __init__(self, vertex_1, vertex_2):
        self._vertex_1 = vertex_1
        self._vertex_2 = vertex_2
        self._coordinates = [vertex_1, vertex_2]
        # Edge will always be either perfectly vertical or perfectly horizontal
        if(vertex_1[0] == vertex_2[0]):
            self._sig_coordinate = vertex_1[0]
            self._vertical = True
        else:
            self._sig_coordinate = vertex_1[1]
            self._vertical = False
    
    @property
    def vertex_1(self):
        return self._vertex_1
    @property
    def vertex_2(self):
        return self._vertex_2
    @property
    def vertical(self):
        return self._vertical
    @property
    def coordinates(self):
        return self._coordinates
    @property
    def sig_coordinate(self):
        # The significant coordinate could be the x or y value of the edge.
        # This depends on if the edge is vertical
        return self._sig_coordinate
    @property
    def data(self):
        # The significant coordinate could be the x or y value of the edge.
        # This depends on if the edge is vertical
        return {
            "sig_coordinate": self._sig_coordinate,
            "vertex_1": self._vertex_1,
            "vertex_2": self._vertex_2,
            "coordinates": self._coordinates,
            "vertical": self._vertical
        }

    def intersects(self, edge_2):
        """Determine if two perpendicular edges intersect (parallel ones are ignored)"""
        if self.vertical != edge_2.vertical:
            if self.vertical:
                intersect_point = [self.sig_coordinate, edge_2.sig_coordinate]
            else:
                intersect_point = [edge_2.sig_coordinate, self.sig_coordinate]
            
            edge_1_type = point_edge_intersect_type(intersect_point, self.coordinates, self.vertical)
            edge_2_type = point_edge_intersect_type(intersect_point, edge_2.coordinates, edge_2.vertical)
            if(edge_1_type == "none" or edge_2_type == "none"):
                return False
            elif(edge_1_type == "vertex" and edge_2_type == "vertex"):
                # Don't report intersection when edges are intersecting at each one's vertex 
                return False
            else:
                return True

        return False



if __name__ == "__main__":
    start = time.time()

    with open("2025/input9test.txt", "r", encoding="utf-8") as file:
        red_tiles = [list(map(int, line.split(","))) for line in file]
    red_tile_count = len(red_tiles)

    # Generate all boundary edges
    bound_edges = [Edge(red_tiles[0], red_tiles[-1])]
    for i in range(0, red_tile_count - 1):
        bound_edges.append(
            Edge(red_tiles[i], red_tiles[i+1])
        )

    # Generate and determine the validity of every possible rect between red tiles
    largest_area = -1
    answer_vertices = []
    for i in range(red_tile_count):
        print(i)
        for j in range(i+1, red_tile_count):
            rect_edges = get_rect_edges(red_tiles[i], red_tiles[j])
            valid_rect = True
            for bound_edge in bound_edges:
                for rect_edge in rect_edges:
                    if(rect_edge.intersects(bound_edge)):
                        valid_rect = False
                        break
                if not valid_rect:
                    break
            if valid_rect:
                area = get_area(red_tiles[i], red_tiles[j])
                if(largest_area < area):
                    answer_vertices = [red_tiles[i], red_tiles[j]]
                largest_area = max(largest_area, area)
    for bound_edge in bound_edges:
        print(bound_edge.data["coordinates"])            
    print(answer_vertices)
    print(f"Answer: {largest_area}")
    print(f"Execution time: {time.time() - start}")
