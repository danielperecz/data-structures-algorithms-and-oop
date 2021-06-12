def bfs(graph, root):
    visited = set(root)
    queue = [root]
    visited_order = []
    while queue:
        vertex = queue.pop(0)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                visited_order.append(neighbour)
    print(" -> ".join(visited_order))


if __name__ == "__main__":
    graph_ = {
        "A": ["B", "C"],    # Node A connected to B & C
        "B": ["D", "E"],    # B connected to D & E
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": []
    }
    bfs(graph_, "A")
