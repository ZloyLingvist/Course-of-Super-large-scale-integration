import networkx as nx
import matplotlib.pyplot as plt
def read_procedure():
    ##### место для ввода данных
    n=10
    #line="1 0 0 1 1 0 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 1 0 0 0 1 0 0 0 0 0 1 0 1 1 0 0 1 1 0 1 0"
    line="0 0 0 0 1 1 1 1 1 0 0 0 0 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
    #n=6
    #line='1 1 1 0 0 1 0 1 0 0 0 1 1 1 1'
    n=6
    line='1 1 1 0 0 1 1 1 1 1 1 1 1 0 1'
    #1 0 0 1 1 0 0 0 0
    #1 0 0 0 1 0 0 0
    #1 0 0 0 1 0 0
    #1 0 0 0 1 0
    #0 0 0 0 1
    #0 1 1 0
    #0 1 1
    #0 1
    #0
    for i in range(n):
        G.add_node(i)

    
    #########        
    line=line.split()
    a,ai,res2,res=[],[],[],[]

    for i in range (n):
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
    for i in range(len(res)):
        for j in range(len(res[i])):
            if res[i][j]==1:
                G.add_edge(i,j)
    #print(res)
    return res


##############################################


def traverse(u,visited,node,subgraph):
    visited[u]=True
    for v in range(node):
        if subgraph[u][v]:
            if not visited[v]:
                traverse(v,visited,node,subgraph)


def isconnected(node,subgraph):
    vis=[]
    for u in range(node):
        for i in range(node):
            vis.append(False)

        traverse(u,vis,node,subgraph)

        for i in range(node):
            if not vis[i]:
                return False

    return True


def fill_subgraph(subgraph,node,u_,v_,dist):
    subgraph_row,subgraph_col=0,0

    for u in range(node):
        subgraph_col=0
        if (u==u_ or u==v_):
            continue
        for v in range(node):
            if (v==v_ or v==u_):
                continue
            subgraph[subgraph_row][subgraph_col]=dist[u][v]
            subgraph_col=subgraph_col+1

        subgraph_row=subgraph_row+1


def isthreeconnected(node,dist):
    subgraph=[]
    for i in range(node-2):
        temp=[]
        for j in range(node-2):
            temp.append(0)
            
        subgraph.append(temp)

    for u in range(node):
        for v in range(u+1,node):
            fill_subgraph(subgraph,node,u,v,dist)
            if not isconnected(node-2,subgraph):
                return False

    return True

def contractedge(v1,v2,graph,graph_contracted,n):
    new_graph=[]
    for i in range(n):
        temp=[]
        for j in range(n):
            temp.append(0)
            
        new_graph.append(temp)

    for i in range(n):
        for j in range(n):
            new_graph[i][j]=graph[i][j]

    new_graph[v1][v2]=new_graph[v2][v1]
    new_graph[v2][v1]=0

    for i in range(n):
        new_graph[i][v1]=new_graph[i][v1]+new_graph[i][v2]
        new_graph[v1][i]=new_graph[v1][i]+new_graph[v2][i]

    subgraph_row,subgraph_col=0,0
    for u in range(n):
        subgraph_col=0
        if u==v2:
            continue
        for v in range(n):
            if v==v2:
                continue
            graph_contracted[subgraph_row][subgraph_col]=new_graph[u][v]
            subgraph_col=subgraph_col+1

        subgraph_row=subgraph_row+1

def refill(graph,contrained_graph,n):
    for i in range(n):
        for j in range(n):
            contrained_graph[i][j]=graph[i][j]


def main():
    graph=read_procedure()
    n=len(graph[0])
    graph_contracted=[]
    for i in range(n):
        temp=[]
        for j in range(n):
            temp.append(0)

        graph_contracted.append(temp)

    if isthreeconnected(n,graph):
        print("3-connected")
        for i in range(n):
            for j in range(n):
                refill(graph,graph_contracted,n)
                if graph[i][j]>0:
                    contractedge(i,j,graph,graph_contracted,n)
                    if isthreeconnected(n,graph_contracted):
                        print(i," ",j)
                        return 0
    else:
        print('not 3 connected')
    
    
G=nx.Graph()
# adding just one node:
#G.add_node("a")
# a list of nodes:
#G.add_nodes_from(["b","c"])
main()
nx.draw(G,with_labels = True)
plt.show() # display                         

