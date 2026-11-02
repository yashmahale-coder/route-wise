import heapq
import math

def dijkstra(graph, start, goal):
    """Return (path, total_cost, number_of_nodes_expanded)."""
    queue = [(0, start)]
    distances = {node: math.inf for node in graph}
    previous = {}
    distances[start] = 0
    visited = 0

    while queue:
        cost, node = heapq.heappop(queue)
        if cost != distances[node]:
            continue
        visited += 1
        if node == goal:
            break
        for neighbor, weight in graph[node].items():
            new_cost = cost + weight
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                previous[neighbor] = node
                heapq.heappush(queue, (new_cost, neighbor))

    if distances[goal] == math.inf:
        return [], math.inf, visited

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = previous[current]
    path.append(start)
    path.reverse()
    return path, distances[goal], visited
