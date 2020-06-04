
#g = Graph(9,[1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,1,1,1,0,1,0,0,0,1,1])
# Check if graph is doubly-connected

class Graph:
    
    def __init__(self, v, i):
        
        self.V = v 
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
                
        return graph
    
    def DFS(self, g, start, visited = None):
        
        visited_vertices = 1
        
        if visited is None:
            
            visited = [False] * (self.V-1)
        
        #print(start)
        
        visited[start] = True
        
        for i in range(0,self.V-1):
            
            if g[start][i] == 1 and not visited[i]:
                
                visited_vertices+=self.DFS(g,i,visited)
        
        return visited_vertices
    
    def is_connected(self,vertex):
        
        
        _graph = [row[:] for row in self.graph]
        
        #print("BEFORE DELETION", _graph)
        del _graph[vertex]
        #print("AFTER ROW DELETION",_graph)
        
        for i in range(0,self.V-1):
            
            del _graph[i][vertex]
            #print(_graph[i][item] is self.graph[i][item])
        
        #print("AFTER COLUMN DELETION",_graph)
        
        return self.DFS(_graph, 0) == (self.V-1)
    
    def check_double(self):
        
        for v in range(self.V):
            
            if not self.is_connected(vertex  = v):
                return False
            
        return True
    
g = Graph(9,[1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,1,0,1,0,0,0,1,1])


if(g.check_double()==True):
    print('Граф двусвязный')
else: print('Графы не двусвязный')