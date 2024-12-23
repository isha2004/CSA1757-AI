import heapq


# Function to calculate the Manhattan distance between the current state and the goal state
def manhattan_distance(state, goal_state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x, y = divmod(state[i][j] - 1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance


# Function to check if a given 8-puzzle configuration is solvable
def is_solvable(state):
    flat_state = [num for row in state for num in row if num != 0]
    inversions = 0
    for i in range(len(flat_state)):
        for j in range(i + 1, len(flat_state)):
            if flat_state[i] > flat_state[j]:
                inversions += 1
    return inversions % 2 == 0


# Function to get all possible neighboring states by moving the blank tile
def get_neighbors(state):
    neighbors = []
    zero_row, zero_col = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)

    for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = zero_row + move[0], zero_col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row[:] for row in state]
            new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], \
            new_state[zero_row][zero_col]
            neighbors.append(new_state)

    return neighbors


# Function to solve the 8-puzzle problem using A* search algorithm
def solve_8_puzzle(start_state, goal_state):
    if not is_solvable(start_state):
        print("The given puzzle is not solvable.")
        return None

    priority_queue = []
    heapq.heappush(priority_queue, (manhattan_distance(start_state, goal_state), start_state, []))
    visited = set()
    visited.add(tuple(tuple(row) for row in start_state))

    while priority_queue:
        cost, current_state, path = heapq.heappop(priority_queue)
        path = path + [current_state]

        if current_state == goal_state:
            return path

        for neighbor in get_neighbors(current_state):
            if tuple(tuple(row) for row in neighbor) not in visited:
                heapq.heappush(priority_queue, (len(path) + manhattan_distance(neighbor, goal_state), neighbor, path))
                visited.add(tuple(tuple(row) for row in neighbor))

    return None


# Example usage
start_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

solution_path = solve_8_puzzle(start_state, goal_state)
if solution_path:
    print("Solution found!")
    for state in solution_path:
        print(state)
else:
    print("No solution exists for the given start state.")