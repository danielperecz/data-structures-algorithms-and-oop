def bfs(graph, root):
    visited = [root]
    queue = [root]
    while queue:
        vertex = queue.pop(0)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    print(" -> ".join(visited))


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
