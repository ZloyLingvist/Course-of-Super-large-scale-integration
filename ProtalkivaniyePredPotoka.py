#https://e-maxx.ru/algo/preflow_push
import networkx as nx
import matplotlib.pyplot as plt


def read_procedure():
    ##### место для ввода данных
    n=6
    line="6 0 6 0 0 3 2 3 0 0 1 3 5 0 7"
    line="6 7 0 0 0 2 3 0 0 3 5 0 2 4 7"
    #line="6 6 0 0 0 2 3 3 0 0 5 0 1 3 7"
    #n=4
    #line="8 5 0 4 3 10"
    #6 0 6 0 0
    #3 2 3 0
    #0 1 3
    #5 0 
    #7
    for i in range(n):
        G1.add_node(i)
        G2.add_node(i)
    
    #####
    
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


    #for i in range(len(res)):
     #   for j in range(len(res[i])):
      #      if res[i][j]!=0:
       #         G.add_edge(i,j,weight=res[i][j])
    #print(res)
    return res

#########################################
inf=10000000

def push(u,v,f,e,c):
    d=min(e[u],c[u][v]-f[u][v])
    f[u][v]=f[u][v]+d
    f[v][u]=(-1)*f[u][v]
    e[u]=e[u]-d
    e[v]=e[v]+d
  

def lift(u,h,f,c):
    d=inf
    for i in range(len(f)):
        if c[u][i]-f[u][i]>0:
            d=min(d,h[i])
    
    if d==inf:
        return 0

    h[u]=d+1
   

def main():
    a=read_procedure()
    f,e,h=[],[],[]
    n=len(a[0])
    
    for i in range(n):
        temp=[]
        e.append(0)
        h.append(0)
        for j in range(n):
            temp.append(0)

        f.append(temp)
    
    for i in range(1,n):
        f[0][i]=a[0][i]
        f[i][0]=-a[0][i]


    h[0]=n
    
    for i in range(1,n):
        e[i]=f[0][i]

    
    step=0

    h_str=""
    e_str=""

    h_arr=[]
    e_arr=[]
    
    while(True):
        print("step: ", step)
        
        for i in range(n):
            h_str=h_str+str(h[i])+" "

        for i in range(n):
            e_str=e_str+str(e[i])+" "

        print("f: ")
        for i in range(n):
            for j in range(n):
                if f[i][j]!=0:
                    if f[i][j]>0:
                        print("(",i,",",j,")=", a[i][j]-f[i][j])
                    else:
                        print("(",i,",",j,")=", (-1)*f[i][j]+f[j][i])

        temp_i=0
        for i in range(1,n-1):
            if e[i]>0:
                temp_i=i
                break

        if temp_i==0:
            h_arr.append(h_str.strip())
            h_str=""
            e_arr.append(e_str.strip())
            e_str=""
            break

        temp_j=n

        for j in range(n):
            if a[temp_i][j]-f[temp_i][j]>0 and h[temp_i]==h[j]+1:
                temp_j=j
                break

        if temp_j<n:
          push(temp_i,temp_j,f,e,a)
        else:
          lift(temp_i,h,f,a)

        h_arr.append(h_str.strip())
        h_str=""
        
        e_arr.append(e_str.strip())
        e_str=""
        step=step+1

    flow=0
    for i in range(n):
        if a[0][i]:
            flow=flow+f[0][i]

    ###вывод h ###
    str1="Таблица h \n"
    for i in range(n):
        if i==0:
            str1=str1+" s"
        if i==n-1:
            str1=str1+" t"
        if i!=0 and i!=n-1:
            str1=str1+" "+str(i)

    print(str1)

    str1=""
    for i in range(len(h_arr)):
        t=h_arr[i].split()
        for j in range(len(t)):
            str1=str1+" "+t[j]

        str1=str1+"\n"

    print(str1)
    #########################
        
    str1="Таблица e \n"
    for i in range(n):
        if i==0:
            str1=str1+" s"
        if i==n-1:
            str1=str1+" t"
        if i!=0 and i!=n-1:
            str1=str1+" "+str(i)

    print(str1)

    str1=""
    for i in range(len(e_arr)):
        t=e_arr[i].split()
        for j in range(len(t)):
            str1=str1+" "+t[j]

        str1=str1+"\n"

    print(str1)
    ###########################
    #print(a)
    print("f:",f)
    print("\n Ответ: \n ", max(flow,0))
    for i in range(n):
            for j in range(n):
                if f[i][j]!=0:
                    if f[i][j]>0:
                        G1.add_edge(i,j,length=a[i][j]-f[i][j])
                        G2.add_edge(i,j,length=f[i][j])
                        print('')
                    else:
                        G1.add_edge(i,j,length=a[i][j]-(-1)*f[i][j]-f[j][i])

    
G1=nx.MultiDiGraph()
G2=nx.MultiDiGraph()
main()

################################################################
'''
pos = nx.spring_layout(G1)
nx.draw(G1, pos)
edge_labels=dict([((u,v,),d['length'])
             for u,v,d in G1.edges(data=True)])
nx.draw_networkx_edge_labels(G1, pos, edge_labels=edge_labels, label_pos=0.3, font_size=12,with_labels = True)

nx.draw(G1,pos, node_color = 'red', node_size=1500,edge_color='red',edge_cmap=plt.cm.Reds,with_labels = True)
#plt.axis('off')
plt.show()
'''
#################################################################
pos = nx.spring_layout(G2)
nx.draw(G2, pos)
edge_labels=dict([((u,v,),d['length'])
             for u,v,d in G2.edges(data=True)])
nx.draw_networkx_edge_labels(G2, pos, edge_labels=edge_labels, label_pos=0.3, font_size=12,with_labels = True)

nx.draw(G2,pos, node_color = 'red', node_size=1500,edge_color='red',edge_cmap=plt.cm.Reds,with_labels = True)
#plt.axis('off')
plt.show()
