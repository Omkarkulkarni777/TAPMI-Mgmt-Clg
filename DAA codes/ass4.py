def dijkstra(input_matrix, source, n):
    MAX_VALUE = float('inf')
    dist = [MAX_VALUE] * n  # Initialize distances to infinity
    visited = [False] * n  # Mark all nodes as not visited

    # Adjust the source index
    source -= 1
    dist[source] = 0  # Set the distance to the source node to 0

    for count in range(n - 1):  # Iterate through all nodes
        u = -1
        for i in range(n):
            # Find the node with the minimum distance among the unvisited nodes
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i

        visited[u] = True  # Mark the selected node as visited

        for v in range(n):
            # Update distances to neighboring nodes if a shorter path is found
            if not visited[v] and input_matrix[u][v] != 0 and dist[u] != MAX_VALUE and dist[u] + input_matrix[u][v] < dist[v]:
                dist[v] = dist[u] + input_matrix[u][v]

    print("Node\tDistance from Source")
    for i in range(n):
        # Adjust the node index and print the final distances
        print(f"{i + 1}\t{dist[i]}")

if __name__ == "__main__":
    n = int(input("Enter the number of nodes: "))
    input_matrix = []

    print("Enter the input matrix (Enter 0 for no connection):")
    for i in range(n):
        row = list(map(int, input().split()))
        input_matrix.append(row)

    source = int(input("Enter the source node: "))

    dijkstra(input_matrix, source, n)
