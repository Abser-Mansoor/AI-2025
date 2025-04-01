import random
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_distance(route, locations):
    return sum(distance(locations[route[i]], locations[route[i+1]]) for i in range(len(route)-1))

def hill_climbing(locations, max_iterations=1000):
    n = len(locations)
    current_route = list(range(n))  # Start with a sequential route
    random.shuffle(current_route)  # Randomize initial route
    current_distance = total_distance(current_route, locations)

    for _ in range(max_iterations):
        best_neighbor = None
        best_distance = current_distance

        for i in range(n):
            for j in range(i + 1, n):
                new_route = current_route[:]
                new_route[i], new_route[j] = new_route[j], new_route[i]  # Swap two locations
                new_distance = total_distance(new_route, locations)

                # Accept the new route if it reduces the total distance
                if new_distance < best_distance:
                    best_neighbor = new_route
                    best_distance = new_distance

        # If no better route is found, stop
        if best_neighbor is None:
            break

        current_route = best_neighbor
        current_distance = best_distance

    return current_route, current_distance

locations = [(0, 0), (2, 3), (5, 4), (6, 1), (8, 7), (1, 6)]
optimized_route, min_distance = hill_climbing(locations)
print("Optimized Route:", optimized_route)
print("Total Distance:", round(min_distance, 2))
