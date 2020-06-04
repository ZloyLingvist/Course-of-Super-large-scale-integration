import queue
from itertools import repeat

INT_MAX=99999
def bfs(residual_graph,s,t,parent,V):
    visited=[]
    for i in range(V):
        visited.append(False)

    q=queue.Queue(maxsize=1000)
    q.put(s)
    visited[s] = True;
    parent[s] = -1;

    while (not q.empty()):
        u = q.get();
        for v in range(V):
            if visited[v] == False and residual_graph[u][v] > 0:
                q.put(v)
                parent[v] = u;
                visited[v] = True

    return (visited[t] == True);

def fordfulkerson(a,s,t,V):
    u=0
    v=0
    max_flow=0
    parent,residual_graph=[],[]
    for u in range(V):
        temp=[]
        parent.append(0)
        for v in range(V):
            temp.append(0)

        residual_graph.append(temp)

    for u in range(V):
        for v in range(V):
            if u!=v:
                residual_graph[u][v]=a[u][v]

    while(bfs(residual_graph,s,t,parent,V)):
          path_flow=INT_MAX
          
          v=t
          while (v!=s):
              u=parent[v]
              path_flow=min(path_flow,residual_graph[u][v])
              v=parent[v]

          v=t
          while (v!=s):
              u=parent[v]
              residual_graph[u][v]=residual_graph[u][v]-path_flow
              residual_graph[v][u]=residual_graph[u][v]+path_flow
              v=parent[v]

          max_flow=max_flow+path_flow

    return max_flow
            

def read_procedure(n,line):
    line=line.split()
    a,ai,res2,res=[],[],[],[]

    for i in range(n):
        for j in range(n):
            ai.append(-1)

        a.append(ai)
        ai=[]
 
    num=n
    
    for i in range(len(line)):
        res2.append(line[i])
        if len(res2)==num-1:
            res2.insert(0,0)
            res.append(res2)
            res2=[]
            num=num-1

    res.append([0])
  
    for i in range(len(res)):
        if len(res[i])!=n:
            while(len(res[i])!=n):
                res[i].insert(0,-1)

    for i in range(len(res)):
        for j in range(len(res[i])):
            if res[i][j]==-1:
                res[i][j]=res[j][i]

            res[i][j]=int(res[i][j])

    print(res)
    return res

def main(a):
    n=len(a[0])
    #min_chosen_t=-1
    min_cut=INT_MAX
    for i in range(1,n):
        result=fordfulkerson(a,0,i,n)
        if result<min_cut:
            min_cut=result
            #min_chosent_t=i

    print(min_cut)
          
n= 6
b="0 1 0 0 0 1 0 0 0 1 0 0 1 1 0"


main(read_procedure(n,b))

