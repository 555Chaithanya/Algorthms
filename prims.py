from heapq import *
def prims(graph,start,parent,dist,visited):
    bag=[]
    heappush(bag,[start,0])
    dist[start]=0
    parent[start]=-1
    while bag:
        n,d37123=heappop(bag)
        if not visited[n]:
            visited[n]=1
            for cd,cn in graph[n]:
                if dist[cn]>cd and not visited[cn]:
                    parent[cn]=n
                    dist[cn]=cd
                    heappush(bag,[cn,cd])
    print(dist)
    print(parent)
ipt=[[1,2,1],[1,3,6],[1,4,5],[2,3,6],[3,5,7],[3,6,3],[4,6,2],[4,7,10],[5,8,12],[6,8,8],[7,8,7],[7,9,3],[8,9,8]]
n=9
graph={}
parent={}
dist={}
visited={}
for i in range(1,n+1):
    graph[i]=[]
    parent[i]=None
    dist[i]=9999
    visited[i]=0
for u,v,d in ipt:
    graph[u].append([d,v])
    graph[v].append([d,u])
start=1
prims(graph,start,parent,dist,visited)
