from itertools import permutations

def tsp_brute_force(distances):
    cities = range(len(distances))
    min_cost = float('inf')
    best_path = []

    for perm in permutations(cities):
        cost = sum(distances[perm[i]][perm[i + 1]] for i in range(len(perm) - 1))
        cost += distances[perm[-1]][perm[0]]  # Return to start

        if cost < min_cost:
            min_cost = cost
            best_path = perm

    return best_path, min_cost

# Distance Matrix Example
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print("TSP Solution:", tsp_brute_force(distances))
