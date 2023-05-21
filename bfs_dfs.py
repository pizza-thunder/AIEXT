#create a graph class and store the edges in the form of adjacency matrix
class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.queue=[]
        self.visited=[]
        self.matrix=[[0 for i in range(vertices)] for j in range(vertices)]
    def create_edge(self,v1,v2):
        self.matrix[v1][v2]=1
        self.matrix[v2][v1]=1
    def DFS(self,i):
        if i not in self.visited:
            self.visited.append(i)
        for x in range(self.vertices):
            if self.matrix[i][x]==1 and x not in self.visited:
                self.DFS(x)
    def BFS(self,i):
        if i not in self.visited:
            self.visited.append(i)
        for x in range(self.vertices):
            if self.matrix[i][x]==1 and x not in self.visited:
                self.queue.append(x)
        if len(self.queue)>=1:
            self.BFS(self.queue.pop(0))

n=int(input("Enter the number of Vertices: ")) 
g=Graph(n)
edges = int(input("Enter the number of edges: "))
for i in range(edges):
    a,b = map(int,input("Enter the nodes connecting a edge: ").split())
    g.create_edge(a,b)

start = int(input("Enter the starting node: "))
print("The bfs traversal is: ")
g.BFS(start)
print(g.visited)
g.visited=[]
print("The dfs traversal is: ")
g.DFS(start)
print(g.visited)
