import math

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

    #print(res)
    return res

def main(mat):
    n,res,minres=0,0,math.exp(10)
    n=len(a[0])
    k=n%2
    if not n%2:
        var=[]
        seen=[]
        gain=[]
        for i in range(n):
            var.append(0)
            seen.append(0)
            gain.append(0)

        print(mat)

        for i in range(int(n/2),n):
            var[i]=1

        cnt=0
        while(True):
            print("Шаг: ",cnt)
            cnt=cnt+1
            max1=-n
            max2=-n
            tmp1=0
            tmp2=0
            for i in range(n): #находим макс гейн для 1 множества
                if not var[i] and not seen[i]:
                    gain[i]=0
                    for j in range(n):
                        if var[j]:
                            gain[i]=gain[i]+mat[i][j]
                        else:
                            gain[i]=gain[i]-mat[i][j]

                    print("В-",i,":",gain[i],"",end = '|')
                    if gain[i]>max1:
                        max1=gain[i]
                        tmp1=i

            #перекидываем максимум из 1 в 2
            var[tmp1]=1
            seen[tmp1]=1
            print()
           
            for i in range(n): #находим макс гейн для 2 множества
                if var[i] and not seen[i]:
                    gain[i]=0
                    for j in range(n):
                        if not var[j]:
                            gain[i]=gain[i]+mat[i][j]
                        else:
                            gain[i]=gain[i]-mat[i][j]

                    print("В-",i,':',gain[i],"",end = '|')
                    if gain[i]>max2:
                        max2=gain[i]
                        tmp2=i

            #перекидываем максимум из 1 в 2
            var[tmp2]=0
            seen[tmp2]=1
            res=0
            for i in range(n):
                if not var[i]:
                    for j in range(n):
                        if var[j] and mat[i][j]:
                            res=res+1

            if res<minres:
                minres=res

            print("\nСрез=",res)
            c=0
            for i in range(n):
                if seen[i]:
                    c=1
                else:
                    c=0
                    break
            if c:
                print("Наим.Срез= ",minres)
                break
                
                
n=6
#line="1 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 1 1 0 0 0 1 0 0 0 0 0 0 1 1 1"
line = "1 0 1 0 0 0 1 0 0 1 1 1 0 0 1"   
        
a=read_procedure(n,line)
main(a)
    
