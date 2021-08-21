class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = {}

    def add_adjacent_vertex(self, vertex, weight):
        self.adjacent_vertices[vertex] = weight


def dijkstra_shortest_path(starting_vertex, final_vertex):
    # Returns a tuple containing the shortest path & the path's weight; (path, weight).

    cheapest_paths = {starting_vertex.value: 0}
    inter_vertex_paths = {}

    unvisited_vertices = [starting_vertex]
    visited_vertices = {}

    current_vertex = starting_vertex
    while current_vertex:
        visited_vertices[current_vertex.value] = True
        unvisited_vertices.remove(current_vertex)

        # Iterate over each vertex of the adjacent vertices.
        for adjacent_vertex, weight in current_vertex.adjacent_vertices.items():
            if (adjacent_vertex.value not in visited_vertices) and (adjacent_vertex not in unvisited_vertices):
                unvisited_vertices.append(adjacent_vertex)

            # Calculate distance and update dictionaries.
            weight_through_current_vertex = cheapest_paths[current_vertex.value] + weight
            if (adjacent_vertex.value not in cheapest_paths) or (weight_through_current_vertex < cheapest_paths[adjacent_vertex.value]):
                cheapest_paths[adjacent_vertex.value] = weight_through_current_vertex
                inter_vertex_paths[adjacent_vertex.value] = current_vertex.value

        # Select vertex with shortest edge.
        current_vertex = sorted(unvisited_vertices, key=lambda vertex: cheapest_paths[vertex.value])
        current_vertex = current_vertex[0] if current_vertex else None

    # Now use inter_vertex_paths to calculate the actual shortest path.
    shortest_path = []
    current_vertex_value = final_vertex.value
    while current_vertex_value != starting_vertex.value:
        shortest_path.append(current_vertex_value)
        current_vertex_value = inter_vertex_paths[current_vertex_value]

    return [starting_vertex.value] + list(reversed(shortest_path)), cheapest_paths[final_vertex.value]


def main():
    atlanta = Vertex("Atlanta")
    boston = Vertex("Boston")
    chicago = Vertex("Chicago")
    denver = Vertex("Denver")
    el_paso = Vertex("El Paso")

    atlanta.add_adjacent_vertex(boston, 100)
    atlanta.add_adjacent_vertex(denver, 160)
    boston.add_adjacent_vertex(chicago, 120)
    boston.add_adjacent_vertex(denver, 180)
    chicago.add_adjacent_vertex(el_paso, 80)
    denver.add_adjacent_vertex(chicago, 40)
    denver.add_adjacent_vertex(el_paso, 140)

    print(dijkstra_shortest_path(atlanta, el_paso))


if __name__ == "__main__":
    main()
