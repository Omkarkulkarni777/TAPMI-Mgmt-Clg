def is_safe(board, x, y, n):
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1

def knight_moves(xi, yi, board, n, count):
    if count == n * n:
        print("Number of jumps:", count)
        for row in board:
            print(row)
        return True
    
    for i in range(8):
        x, y = xi + move_x[i], yi + move_y[i]
        if is_safe(board, x, y, n):
            board[x][y] = count + 1
            if knight_moves(x, y, board, n, count + 1):
                return True
            board[x][y] = -1  # Backtrack if the current move doesn't lead to a solution
    
    return False

if __name__ == "__main__":
    n = int(input("Enter the size of the chessboard (N): "))
    board = [[-1] * n for _ in range(n)]
    
    print("Enter initial position of the knight (x coord):")
    x = int(input())
    print("Enter initial position of the knight (y coord):")
    y = int(input())
    
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    
    board[x][y] = 1
    
    if knight_moves(x, y, board, n, 1):
        print("Yes")
    else:
        print("No")
