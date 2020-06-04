import itertools
import math

def main(cost,mode): ##cost матрица
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
            if mode==1:
                print(a+1,b+1," ",end="")
            edge_count=edge_count+1
            mincost=mincost+minim

        return mincost

    return kruskall(cost)
       
                  
def read(a,mode):
    temp=[]
    matrix=[]
    c = [" ".join((v, g)) for v,g in zip(a[:-1:2], a[1::2])]
    n=len(c)
    
    for i in range(n):
        temp=[]
        for j in range(n):
            temp.append(0)

        matrix.append(temp)

    for i in range(len(c)):
        for j in range(i+1,len(c)):
            a=c[i].split()
            b=c[j].split()
            matrix[i][j]=abs(int(a[0])-int(b[0]))+abs(int(a[1])-int(b[1]))
            matrix[j][i]=matrix[i][j]

    res=[] 
    res=main(matrix,mode)
    return res

def before_read(a):
    #
    n=5
    #
    mystr=a
    b=[]
    a1=a.split()
    i=0
    j=0
    while(i<len(a1)):
        a1[i]=int(a1[i])
        j=1
        while(j<len(a1)):
          a1[j]=int(a1[j])
          if i!=j-1:
              b.append([a1[i],a1[j]])

          j=j+2
          
        i=i+2

    ####
    save_coord=a
    save_res=read(a.split(),0)
    
    weight=save_res
    length_subset=999999

    str1=""
    test_list=[]
    for L in range(n):
        if(L > n-1):
            break

        for subset in itertools.combinations(b,L):
                joined = ' '.join(' '.join(map(str, row)) for row in list(subset))
                test=mystr+" "+joined
                test_list.append(test)

                tmp_res=read(test.split(),0)
        
                if tmp_res<weight:
                    weight=tmp_res
                    save_coord=test
                    length_subset=len(list(subset))

                if tmp_res==weight:
                    if len(list(subset))<length_subset:
                        weight=tmp_res
                        save_coord=test
                        length_subset=len(list(subset))
                  
            

    print('Минималный вес',weight)
    print('Координаты',save_coord)
    print('Ответ:')
    tmp_res=read(save_coord.split(),1)
    
  
a="0 3 1 1 3 0 4 2 2 4"             
before_read(a)    
  
	
