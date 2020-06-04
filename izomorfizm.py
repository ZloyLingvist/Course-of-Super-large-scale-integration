
#g1 = Tree(9,[0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,1,0,0,0,0])
#g2 = Tree(9,[1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0])
# Tree class to check isomorphism

import numpy as np
from itertools import permutations

class Tree:
    
    def __init__(self, v, i):
        
        self.V = v 
        #self.G = nx.Graph()
        self.items = i
        self.graph = self.build_graph(vertices = self.V,items = self.items)
    
    def build_graph(self, vertices, items): 
        
        if len(items) < (vertices-1) * vertices / 2:
            return "Wrong length"

        graph = [[0 for column in range(vertices)] for row in range(vertices)]
        k = 0
        
        for i in range(0,vertices):
            
            for j in range(i+1,vertices):
                
                
                graph[i][j] = items[k]
                k+=1       
                graph[j][i] = graph[i][j]
        #print(graph)        
        return graph
    
    def DFS(self, start, visited):
        
        if visited is None:
            visited = [False] * self.V
        
        print(start)
        
        visited[start] = True
        
        for i in range(0,self.V):
            if self.graph[start][i] == 1 and not visited[i]:
                self.DFS(i,visited)
                
                
# Check if two trees are isomorphic

def check_isomorphism(g1,g2):
    
    perms = []
    
    eye = np.eye(g1.V)
    
    for item in permutations(eye):
        perms.append(item)
        
    print(len(perms))    
    for item in perms:
        
        temp = np.array(item).dot(np.array(g1.graph)).dot(np.array(item).T)
        #print(temp)
        if np.array_equal(temp,np.array(g2.graph)):
            return True
    
    return False


#n*(n-1)/2 Элементов
#Перестановочная матрица утверждение
g1 = Tree(9,[0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,1,0,0,0,0])
g2 = Tree(9,[1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0])

if(check_isomorphism(g1,g2)==True):
    print('Графы изоморфны')
else: print('Графы неизоморфны')