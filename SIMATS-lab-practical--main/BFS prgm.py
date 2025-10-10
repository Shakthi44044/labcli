def dfs_shortest_path(adj, start, target):
    """
    adj: dict node -> list of neighbors
    start, target: nodes
    returns: a path from start to target (DFS does not guarantee shortest)
    """
    if start == target:
        return [start]

    stack = [start]
    visited = {start}
    parent = {start: None}

    while stack:
        u = stack.pop()  # DFS uses LIFO (stack)
        for v in adj.get(u, []):
            if v not in visited:
                visited.add(v)
                parent[v] = u
                if v == target:
                    # reconstruct path
                    path = [v]
                    while parent[path[-1]] is not None:
                        path.append(parent[path[-1]])
                    path.reverse()
                    return path
                stack.append(v)
    return None

# ----------------------------
if __name__ == "__main__":
    graph = {
        'A': ['B','C'],
        'B': ['A','D','E'],
        'C': ['A','F'],
        'D': ['B'],
        'E': ['B','F'],
        'F': ['C','E']
    }
    print(dfs_shortest_path(graph, 'A', 'F'))
