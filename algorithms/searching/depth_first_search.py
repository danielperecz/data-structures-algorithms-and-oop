def recursive_dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            recursive_dfs(graph, n, visited)
    return visited


def iterative_dfs(graph, root):
    visited = set()
    traversal = []
    stack = [root]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal.append(vertex)
            stack.extend(reversed(graph[vertex]))
    return traversal


if __name__ == "__main__":
    graph_ = {
        "A": ["B", "S"],
        "B": ["A"],
        "C": ["D", "E", "F", "S"],
        "D": ["C"],
        "E": ["C", "H"],
        "F": ["C", "G"],
        "G": ["F", "S"],
        "H": ["E", "G"],
        "S": ["A", "C", "G"]
    }

    recursive_dfs_output = recursive_dfs(graph_, "A", [])
    iterative_dfs_output = iterative_dfs(graph_, "A")

    print("Recursive DFS: {}".format(" -> ".join(recursive_dfs_output)))
    print("Iterative DFS: {}".format(" -> ".join(iterative_dfs_output)))
