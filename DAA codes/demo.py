
def is_safe(x,y,board,n):
    return 0<=x<n and 0<=y<n and board[x][y] == -1

def knight_tour(xi,yi,board,n,count):
    
    if count == n*n:
        print("no of jumps: ",count)
        for row in board:
            print(row)
        return True

    for i in range(8):
        
        x,y = xi + move_x[i], yi+move_y[i]
        
        if is_safe(x,y,board,n):
            
            board[x][y] = count+1
            
            if knight_tour(x,y,board,n,count+1):
                return True
            board[x][y]=-1
    
    return False


if __name__ == "__main__":
    
    n = int(input("Enter size of chess: "))
    
    x= int(input("Enter x coord: "))
    y= int(input("Enter y coord: "))
    
    board = [[-1]*n for _ in range(n)]
    
    move_x = [-2,-2,-1,-1,1,1,2,2]
    move_y = [-1,1,-2,2,-2,2,-1,1]
    
    board[x][y]=1
    
    if knight_tour(x,y,board,n,1):
        print("yessss")
    else:
        print("noooooooooo")