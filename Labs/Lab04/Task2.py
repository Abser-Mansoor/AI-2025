from queue import PriorityQueue
import random

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

def dynamic_a_star(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    frontier = PriorityQueue()
    frontier.put((0, start, []))  # (cost, position, path)
    visited = set()
    costs = {start: 0}
    
    while not frontier.empty():
        curr_cost, curr_pos, curr_path = frontier.get()
        
        if curr_pos in visited:
            continue
        
        visited.add(curr_pos)
        new_path = curr_path + [curr_pos]
        
        if curr_pos == goal:
            return new_path
        
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_pos = (curr_pos[0] + dx, curr_pos[1] + dy)
            if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and maze[new_pos[0]][new_pos[1]] == 0:
                new_cost = curr_cost + random.randint(1, 10)  # Dynamic cost update
                if new_pos not in costs or new_cost < costs[new_pos]:
                    costs[new_pos] = new_cost
                    priority = new_cost + heuristic(new_pos, goal)
                    frontier.put((priority, new_pos, new_path))
    
    return "Path Not Found"

# 1 Being inaccessible
maze = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goals = [(4, 4), (0, 3), (3, 1)]

path_dynamic_astar = dynamic_a_star(maze, start, (4, 4))

print("Dynamic A* Path:", path_dynamic_astar)
