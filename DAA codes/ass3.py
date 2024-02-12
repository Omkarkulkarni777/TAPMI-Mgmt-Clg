INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    
    #create a shallow copy of graph
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

def main():
    try:
        n = int(input("Enter the number of offices: "))

        # Initialize a graph with all edges set to a large number
        graph = [[INF] * n for _ in range(n)] #set for loop just for outer loop

        # Input the cost to connect each pair of offices
        for i in range(n):
            for j in range(n):
                if i != j:
                    cost_str = input(f"Enter the cost to connect office {i + 1} and office {j + 1}: ")
                    # Use a large number if the input is not "inf"
                    graph[i][j] = float('inf') if cost_str.lower() == 'inf' else int(cost_str)

        # Apply Floyd-Warshall algorithm
        result = floyd_warshall(graph)

        
        # Display the minimum cost matrix
        print("\nMinimum cost matrix:")
        for row in result:
            print(row)

    except ValueError:
        print("Invalid input. Please enter valid integers.")


if __name__ == "__main__":
    main()
