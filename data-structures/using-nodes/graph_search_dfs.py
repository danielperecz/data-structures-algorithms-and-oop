class Vertex:
    def __init__(self, value):
        self.value = str(value)
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex):
        # Undirected graph (self & vertex are mutually connected).
        if vertex not in self.adjacent_vertices:
            self.adjacent_vertices.append(vertex)
            vertex.add_adjacent_vertex(self)


def dfs(vertex, search_value, visited_vertices=None):
    if visited_vertices is None:
        visited_vertices = {}

    if vertex.value == search_value:
        return vertex

    visited_vertices[vertex.value] = True
    print(f"Visiting {vertex.value}, while searching for {search_value}.")

    for adjacent_vertex in vertex.adjacent_vertices:
        if adjacent_vertex.value not in visited_vertices:
            if adjacent_vertex.value == search_value:
                return adjacent_vertex
            desired_vertex = dfs(adjacent_vertex, search_value, visited_vertices)
            if desired_vertex:
                return desired_vertex

    return None


def dfs_traversal(vertex, visited_vertices=None):
    if visited_vertices is None:
        visited_vertices = {}

    visited_vertices[vertex.value] = True
    print(f"Visiting {vertex.value}.")

    for adjacent_vertex in vertex.adjacent_vertices:
        if adjacent_vertex.value not in visited_vertices:
            dfs_traversal(adjacent_vertex, visited_vertices)
