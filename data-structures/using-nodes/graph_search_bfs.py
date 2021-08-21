import collections


class Vertex:
    def __init__(self, value):
        self.value = str(value)
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex):
        # Undirected graph (self & vertex are mutually connected).
        if vertex not in self.adjacent_vertices:
            self.adjacent_vertices.append(vertex)
            vertex.add_adjacent_vertex(self)


def bfs_traversal(vertex):
    queue = collections.deque()
    queue.append(vertex)

    visited_vertices = {vertex.value: True}
    while queue:
        current_vertex = queue.popleft()
        print(f"Visiting {current_vertex.value}.")

        for adjacent_vertex in current_vertex.adjacent_vertices:
            if adjacent_vertex.value not in visited_vertices:
                visited_vertices[adjacent_vertex.value] = True
                queue.append(adjacent_vertex)
