graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
    }
dfs_visited=set()
def dfs(dfs_visited,graph,node):
    if node not in dfs_visited:
        print(node,end=" ")
        dfs_visited.add(node)
        for neighbour in graph[node]:
            dfs(dfs_visited,graph,neighbour)
bfs_visited=[]
queue=[]
def bfs(bfs_visited,graph,node):
    bfs_visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end="")
        for neighbour in graph[m]:
            if neighbour not in bfs_visited:
                bfs_visited.append(neighbour)
                queue.append(neighbour)
print("Choose an option from the folllowing:")
print("1.DFS 2.BFS 3.EXIT")
flag=0
while(flag==0):
    choice = int(input("\n Choose your option:"))
    if(choice == 1):
        print("following is the dfs search:")
        dfs(dfs_visited,graph,'5')
    elif(choice == 2):
        print("Following is BFS :")
        bfs(bfs_visited,graph,'5')
    else:
        flag=1
        print("Exiting..")
        
        
