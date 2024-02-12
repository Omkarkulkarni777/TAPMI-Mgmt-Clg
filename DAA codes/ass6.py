import heapq
import copy

class Node:
    def __init__(self, cost, level, assigned, visited):
        self.cost = cost
        self.level = level
        self.assigned = assigned.copy()
        self.visited = visited.copy()

    def __lt__(self, other):
        return self.cost < other.cost

def find_min_cost(mat):
    n = len(mat)
    assigned = [-1] * n
    visited = [False] * n
    pq = [Node(0, -1, assigned, visited)]

    while pq:
        min_node = heapq.heappop(pq)
        i = min_node.level + 1

        if i == n:
            print_assignment(min_node, mat)
            return min_node.cost

        for j in range(n):
            if not min_node.visited[j]:
                new_assigned = copy.copy(min_node.assigned)
                new_visited = copy.copy(min_node.visited)
                new_assigned[i] = j
                new_visited[j] = True
                child = Node(min_node.cost + mat[i][j], i, new_assigned, new_visited)
                heapq.heappush(pq, child)

    return -1

def print_assignment(min_node, mat):
    for i, club in enumerate(min_node.assigned):
        cost = mat[i][club]
        print(f"Student {i+1} is assigned to Club {club+1} with cost {cost}")

    print("Min_Cost:", min_node.cost)

if __name__ == "__main__":
    print("Enter the size of matrix:")
    n = int(input())
    mat = []

    print("Enter the matrix:")
    for _ in range(n):
        row = list(map(int, input().split()))
        mat.append(row)

    min_cost = find_min_cost(mat)
    print("Optimal Solution Cost:", min_cost)
