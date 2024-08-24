import heapq
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}
    
    def add_edges(self, vertex1, vertex2, weight):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1][vertex2] = weight
            self.graph[vertex2][vertex1] = weight
        else:
            print(f"Both vertex1 and vertex2 not found.")

    def display(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {','.join(f'{neigh}, ({wt})' for neigh, wt in edges.items())}")

    def shortest_path(self, start,end):
        queue = [(0, start)]
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        previous_nodes = {vertex: None for vertex in self.graph} 

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)
            
            if current_distance > distances[current_vertex]:
                continue
            for neighbor , weight in self.graph[current_vertex].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_vertex
                    heapq.heappush(queue, (distance, neighbor))

        path = []
        while end is not None:
            path.append(end)
            end = previous_nodes[end]

        return path[::-1], distances[path[0]]

g = Graph()

g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

g.add_edges('A', 'B', 1)
g.add_edges('A', 'C', 4)
g.add_edges('B', 'C', 2)
g.add_edges('C', 'D', 1)

g.display()

path, distance = g.shortest_path('A', 'D')
print(f"\nShortest path from A to D: {' -> '.join(path)} with distance {distance}")


