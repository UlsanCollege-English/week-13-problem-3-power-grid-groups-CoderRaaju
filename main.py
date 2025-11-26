

def count_power_groups(stations, lines):
    """
    Count how many connected groups of power stations exist.

    stations: list of station name strings.
    lines: list of (a, b) pairs, meaning there is an undirected line between a and b.

    Return: integer number of connected components (groups) in the network.
    """

    # TODO Step 1–3: Make sure you understand "power group" and the inputs/outputs.
    # TODO Step 4: Decide how to store neighbors (graph representation).
    # TODO Step 5: Write pseudocode for traversing the graph and counting groups.
    # TODO Step 6: Implement a graph traversal (DFS or BFS) to explore groups.
    # TODO Step 7: Test on small graphs (1 node, chain, completely separate nodes).
    # TODO Step 8: Check that your solution is roughly O(n + m).
    pass


if __name__ == "__main__":
    # Optional manual test
    stations = ["A", "B", "C", "D"]
    lines = [("A", "B"), ("B", "C")]
    print(count_power_groups(stations, lines))  # expected 2
