from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            # Process the node here
            print(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph representation (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A','E','F'],
    'D': ['B'],
    'E': ['C' ],
    'F': [ 'C']
}

start_node = 'A'
bfs(graph, start_node)