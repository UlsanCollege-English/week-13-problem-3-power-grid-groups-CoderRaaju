def count_power_groups(stations, lines):
    """
    Count how many connected groups of power stations exist.

    stations: list of station name strings.
    lines: list of (a, b) pairs for undirected connections.

    Return: integer number of connected components.
    """

    # Build adjacency list
    graph = {s: [] for s in stations}

    for a, b in lines:
        if a in graph and b in graph:
            graph[a].append(b)
            graph[b].append(a)

    visited = set()
    groups = 0

    # DFS function
    def dfs(start):
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)

    # Count connected components
    for station in stations:
        if station not in visited:
            dfs(station)
            groups += 1

    return groups


if __name__ == "__main__":
    # Optional manual test
    stations = ["A", "B", "C", "D"]
    lines = [("A", "B"), ("B", "C")]
    print(count_power_groups(stations, lines))  # expected 2
