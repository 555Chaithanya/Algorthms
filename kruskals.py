def find(graph,node):
    if graph[node]<0:
        return node
    else:
        temp=find(graph,graph[node])
        return temp
def union(graph,a,b,ans):
    ta=a
    tb=b
    a=find(graph,a)
    b=find(graph,b)
    if a==b:
        pass
    else:
        ans.append([ta,tb])
        if graph[a]==graph[b]:
            graph[b]=graph[b]+graph[a]
            graph[a]=b
        else:
            if graph[a]<graph[b]:
                graph[a]=graph[a]+graph[b]
                graph[b]=a
            else:
                graph[b]=graph[b]+graph[a]
                graph[a]=b

ipt=[[1,2,1],[1,3,7],[1,4,10],[1,5,5],[2,3,3],[3,4,4],[4,5,2]]
n=5
ans=[]
ipt=sorted(ipt,key=lambda ipt:ipt[2])
G=[-1]*(n+1)
for u,v,d in ipt:
    union(G,u,v,ans)
for item in ans:
    print(item)
