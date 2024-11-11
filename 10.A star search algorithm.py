import heapq

def a_star_search(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))
    g_costs = {start: 0}
    came_from = {start: None}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1], g_costs[goal]

        for neighbor, cost in graph[current]:
            new_cost = g_costs[current] + cost
            if neighbor not in g_costs or new_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current

    return None, float('inf')


# Example heuristic: Manhattan distance
def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


# Example usage
graph = {
    (0, 0): [((1, 0), 1), ((0, 1), 1)],
    (1, 0): [((0, 0), 1), ((1, 1), 1)],
    (0, 1): [((0, 0), 1), ((1, 1), 1)],
    (1, 1): [((1, 0), 1), ((0, 1), 1), ((2, 1), 1)],
    (2, 1): [((1, 1), 1), ((2, 2), 1)],
    (2, 2): [((2, 1), 1)]
}

start = (0, 0)
goal = (2, 2)

path, cost = a_star_search(graph, start, goal, heuristic)
print(f"Path: {path}")
print(f"Total Cost: {cost}")