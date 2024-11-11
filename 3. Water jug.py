
from collections import deque
def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque()
    queue.append((0, 0))
    while queue:
        current = queue.popleft()
        jug1, jug2 = current
        print(f"Jug1: {jug1}, Jug2: {jug2}")
        if jug1 == target or jug2 == target:
            print(f"Found solution: Jug1: {jug1}, Jug2: {jug2}")
            return True
        if current in visited:
            continue
        visited.add(current)
        queue.append((jug1_capacity, jug2))
        queue.append((jug1, jug2_capacity))
        queue.append((0, jug2))
        queue.append((jug1, 0))
        pour_to_jug2 = min(jug1, jug2_capacity - jug2)
        queue.append((jug1 - pour_to_jug2, jug2 + pour_to_jug2))
        pour_to_jug1 = min(jug2, jug1_capacity - jug1)
        queue.append((jug1 + pour_to_jug1, jug2 - pour_to_jug1))
    print("No solution exists.")
    return False
jug1_capacity = 4  # Capacity of Jug1
jug2_capacity = 3  # Capacity of Jug2
target_amount = 2  # The target amount of water
water_jug_bfs(jug1_capacity, jug2_capacity, target_amount)
