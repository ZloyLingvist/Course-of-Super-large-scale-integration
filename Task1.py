def read_procedure():
    INT_MAX=9999999
    print('Введите n')
    n=int(input())
    a,ai,res2,res=[],[],[],[]

    for i in range(n):
        for j in range(n):
            ai.append(-1)

        a.append(ai)
        ai=[]

    print('Введите строку с весами через пробел')
    line=input().split()
    num=n
    
    for i in range(len(line)):
        res2.append(line[i])
        if len(res2)==num-1:
            res2.insert(0,INT_MAX)
            res.append(res2)
            res2=[]
            num=num-1

    res.append([INT_MAX])
  
    for i in range(len(res)):
        if len(res[i])!=n:
            while(len(res[i])!=n):
                res[i].insert(0,-1)

    for i in range(len(res)):
        for j in range(len(res[i])):
            if res[i][j]=='0':
                res[i][j]=INT_MAX
            if res[i][j]==-1:
                res[i][j]=res[j][i]

            res[i][j]=int(res[i][j])

    print(res)
    return res


def main_procedure(cost):
    parent=[]
    INT_MAX=9999999
    V=len(cost)
    
    def find(i):
        while(parent[i]!=i):
            i=parent[i]
        return i

    def union(i,j):
        a=find(i)
        b=find(j)
        parent[a]=b

    def kruskall(cost):
        mincost=0
        for i in range(V):
            parent.append(i)

        edge_count=0
        while(edge_count<V-1):
            minim=INT_MAX
            a=-1
            b=-1
            for i in range(V):
                for j in range(V):
                    if find(i)!=find(j) and cost[i][j]<minim:
                        minim=cost[i][j]
                        a=i
                        b=j
        
            union(a,b)
            print(a+1,b+1)
            edge_count=edge_count+1
            mincost=mincost+minim

        print(mincost)

    kruskall(cost)
        
a=read_procedure()
main_procedure(a)
