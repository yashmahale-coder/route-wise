import heapq
import math

def heuristic(coords, node, goal):
    x1, y1 = coords[node]
    x2, y2 = coords[goal]
    # Coordinates are in abstract map units; scale to illustrative km.
    return math.hypot(x2 - x1, y2 - y1) / 20

def astar(graph, coords, start, goal):
    """Return (path, total_cost, number_of_nodes_expanded)."""
    queue = [(heuristic(coords, start, goal), 0, start)]
    g_score = {node: math.inf for node in graph}
    previous = {}
    g_score[start] = 0
    visited = 0

    while queue:
        _, cost, node = heapq.heappop(queue)
        if cost != g_score[node]:
            continue
        visited += 1
        if node == goal:
            break
        for neighbor, weight in graph[node].items():
            new_cost = cost + weight
            if new_cost < g_score[neighbor]:
                g_score[neighbor] = new_cost
                previous[neighbor] = node
                priority = new_cost + heuristic(coords, neighbor, goal)
                heapq.heappush(queue, (priority, new_cost, neighbor))

    if g_score[goal] == math.inf:
        return [], math.inf, visited

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = previous[current]
    path.append(start)
    path.reverse()
    return path, g_score[goal], visited
