from itertools import permutations

# Define the function to check if the current permutation solves the puzzle
def is_solution(permutation):
    s, e, n, d, m, o, r, y = permutation
    send = s * 1000 + e * 100 + n * 10 + d
    more = m * 1000 + o * 100 + r * 10 + e
    money = m * 10000 + o * 1000 + n * 100 + e * 10 + y
    return send + more == money

# Define the main function to solve the puzzle
def solve_cryptarithmetic():
    # All unique letters in the puzzle
    letters = 'SENDMORY'

    # Generate all permutations of digits 0-9 taken 8 at a time
    for permutation in permutations(range(10), len(letters)):
        # Ensure 'M' is not zero (since MONEY is a 5-digit number)
        if permutation[letters.index('M')] == 0:
            continue

        # Check if the permutation is a valid solution
        if is_solution(permutation):
            solution = dict(zip(letters, permutation))
            print("Solution found:")
            print(f"SEND + MORE = MONEY")

            # Print the letter to digit mapping
            for letter in letters:
                print(f"{letter} = {solution[letter]}")

            # Calculate and print the numerical values of SEND, MORE, and MONEY
            send = solution['S'] * 1000 + solution['E'] * 100 + solution['N'] * 10 + solution['D']
            more = solution['M'] * 1000 + solution['O'] * 100 + solution['R'] * 10 + solution['E']
            money = solution['M'] * 10000 + solution['O'] * 1000 + solution['N'] * 100 + solution['E'] * 10 + solution['Y']

            print(f"\nNumerical values:")
            print(f"SEND  = {send}")
            print(f"MORE  = {more}")
            print(f"MONEY = {money}")
            
            return solution

    print("No solution found.")
    return None

# Run the solver
solve_cryptarithmetic()