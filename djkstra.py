#python3
class Graph:
    def __init__(self,vertices):
        self.n=vertices
        self.graph=[[] for i in range(n)]
    def addEdge(self,start,end,weight):
        self.graph[start].append([end,weight])
    def Djkstra(self,start,visited):
        weights=[float('inf') for i in self.graph]
        weights[start]=0
        q=[start]
        j=0
        while(len(q)>0 and j<self.n):
            current_point=q.pop(0)
            j+=1
            visited[current_point]=True
            for i in self.graph[current_point]:
                if(weights[i[0]]==float('inf')):
                    weights[i[0]]=weights[current_point]+i[1]
                    q.append(i[0])
                elif(weights[current_point]+i[1]<int(weights[i[0]])):
                    weights[i[0]]=weights[current_point]+i[1]
                    q.append(i[0])
        if(len(q)>0):
            return False
        return True
[n,m]=[int(i) for i in input().split()]
obj=Graph(n)
for i in range(m):
    [x,y,z]=[int(i) for i in input().split()]
    obj.addEdge(x-1,y-1,z)
visited=[False for i in range(n)]
boolean=True
for i in range(n):
    if(not visited[i]):
        boolean=obj.Djkstra(i,visited)
        if(not boolean):
            print('1')
            break
if(boolean):
    print('0')
    
