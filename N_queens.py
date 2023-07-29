global IN
def Issafe(board,row,col):
    for i in range(col):
        if board[row][i]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
           return False
    for i,j in zip(range(row ,IN,1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    return True

def Solve(board,col):
    if col>=IN:
        return True
    for i in range(IN):
        if(Issafe(board,i,col)):
            board[i][col]=1
            if Solve(board,col+1)==True :
               return True
            board[i][col]=0
    return False

def PrintMatrix(board):
    for i in range(IN):
        for j in range(IN):
            print(board[i][j],end=" ")
        print("\n")
        
IN =int(input("Enter no.of queens:"))
board=[[0 for i in range(IN)] for j in range(IN)]

if Solve(board,0)==False:
   print("No solution found")
else:
    PrintMatrix(board)
               
           
        
        
            
        
