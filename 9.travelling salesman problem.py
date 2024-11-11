import itertools

def tsp(cities, start_city):
    all_cities = cities.copy()
    all_cities.remove(start_city)

    min_path = None
    min_dist = float('inf')

    for perm in itertools.permutations(all_cities):
        path = [start_city] + list(perm) + [start_city]
        dist = 0

        for i in range(len(path) - 1):
            dist += graph[path[i]][path[i + 1]]

        if dist < min_dist:
            min_dist = dist
            min_path = path

    return min_path, min_dist


# Define the graph with distances between cities
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

start_city = 'A'
cities = ['A', 'B', 'C', 'D']

shortest_path, shortest_distance = tsp(cities, start_city)
print("Shortest Path:", shortest_path)
print("Shortest Distance:", shortest_distance)