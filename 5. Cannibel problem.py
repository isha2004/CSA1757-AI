from collections import deque

def is_valid_state(m, c):
    # m: missionaries, c: cannibals
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    # Check on the starting side
    if m > 0 and m < c:
        return False
    # Check on the other side
    if (3 - m) > 0 and (3 - m) < (3 - c):
        return False
    return True

def successors(state):
    m, c, b = state
    moves = []
    if b == 1:  # Boat on the starting side
        possible_moves = [(-1, 0), (0, -1), (-2, 0), (0, -2), (-1, -1)]
    else:  # Boat on the other side
        possible_moves = [(1, 0), (0, 1), (2, 0), (0, 2), (1, 1)]

    for dm, dc in possible_moves:
        new_state = (m + dm, c + dc, 1 - b)  # Move boat to the other side
        if is_valid_state(new_state[0], new_state[1]):
            moves.append(new_state)

    return moves


def bfs():
    start_state = (3, 3, 1)  # (missionaries, cannibals, boat)
    goal_state = (0, 0, 0)  # Goal: All missionaries and cannibals on the other side
    visited = set()
    queue = deque([(start_state, [])])

    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path + [state]
        if state not in visited:
            visited.add(state)
            for succ in successors(state):
                queue.append((succ, path + [state]))

    return None


# Run the BFS to find the solution
solution = bfs()
if solution:
    for i, state in enumerate(solution):
        print(f"Step {i}: {state}")
else:
    print("No solution found.")
