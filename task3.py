import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v, weight):
        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:
            self.edges[v] = []
        self.edges[u].append((v, weight))
        self.edges[v].append((u, weight))  # Якщо граф неорієнтований

def dijkstra(graph, start):
    # Ініціалізація
    distances = {vertex: float('infinity') for vertex in graph.edges}
    distances[start] = 0
    priority_queue = [(0, start)]  # (відстань, вершина)
    heapq.heapify(priority_queue)
    visited = set()

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        # Оновлення відстаней до сусідів
        for neighbor, weight in graph.edges[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Приклад використання
g = Graph()
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 1)

start_vertex = 'A'
distances = dijkstra(g, start_vertex)

for vertex in distances:
    print(f"Відстань від {start_vertex} до {vertex} дорівнює {distances[vertex]}")
