n=int(input("Enter no of verteces:"))
def solution(n,d):
    print("output matrix is:")
    for i in range(n):
        for j in range(n):
            if (d[i][j]==9999):
                print("inf",end=" ")
            else:
                print(d[i][j],end=" ")
        print("\n")
def Shpath(n,G):
    d=G
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
        print("A",k+1,":")
        solution(n,d)
print("Enter distance b\w verteces:")
print("!!If there exist no edge b\w verteces enter 9999!!")
G=[[int(input()) for i in range(n)] for j in range(n)]
print("The shortest path is in the form of matrix:")
Shpath(n,G)
