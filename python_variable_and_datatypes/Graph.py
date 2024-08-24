class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edges(self, vertex1, vertex2):
        if vertex1 in self.graph:
            if vertex2 in self.graph:
                self.graph[vertex1].append(vertex2)
                self.graph[vertex2].append(vertex1)
            else:
                print(f"vertex {vertex2} is not found")
        else:
            print(f"vertex {vertex1} is not found")
    
    def display(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {','.join(edges)}")

g = Graph()

g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

g.add_edges('A', 'B')
g.add_edges('A','C')
g.add_edges('B','C')
g.add_edges('C', 'D')

g.display()