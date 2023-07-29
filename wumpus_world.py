maze=[['ste','ok','bre','pit'],
    ['wum','gsb','pit','bre'],
    ['ste','ok','bre','ok'],
    ['agent','bre','pit','bre']]
i=3
j=0
flag=True

print("<--Instructions-->")
print("Enter:\n", "'L' for left\n","'R' for Right\n","'U' for Up\n","'D' for Down\n")

def printArr(arr):
    
    print()
    for k in range(4):
        for l in range(0,4,1):
            print(arr[k][l],end="    ")
        print()
        print()
    print()
    pos(maze)
    
def pos(maze):
    print("You are in( ["+str(i)+"]"+"["+str(j)+"] )th position i.e. at ",str(maze[i][j]))
    
printArr(maze)


while(flag==True):
    move=input("Enter your move: ")
    if move=='U':
        i=i-1
        if(i<0):
            print("you cant make that move")
            i=i+1
    elif(move=='D'):
        i=i+1
        if(i>3):
            print("you cant make that move")
            i=i-1
    elif(move=='L'):
        j=j-1
        if(j<0):
            print("you cant make that move")
            j=j+1
    elif(move=='R'):
        j=j+1
        if(j>3):
            print("you cant make that move")
            j=j-1
    else:
        print("Please enter a valid instruction")
    flag=True
    if(str(maze[i][j])=='pit'):
        pos(maze)
        print("Oops..! Your Game Over")
        flag=False
        break
    elif(str(maze[i][j])=='wum'):
        pos(maze)
        print("Oops..! Your Game Over")
        flag=False
        break
    elif(str(maze[i][j])=='gsb'):
        pos(maze)
        print("You won the jackpot-> gold!!")
        flag=False
        break
    print()
    print()
    printArr(maze)
    
