from queue import PriorityQueue

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

def best_first_search(maze, start, goals):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    path = []
    current_pos = start
    
    while goals:
        frontier = PriorityQueue()
        frontier.put((0, current_pos, []))  # (priority, position, path)
        local_visited = set()
        found = False
        
        while not frontier.empty() and not found:
            _, curr, curr_path = frontier.get()
            
            if curr in local_visited:
                continue
            
            local_visited.add(curr)
            new_path = curr_path + [curr]
            
            if curr in goals:
                goals.remove(curr)
                path.extend(new_path[1:])  # Add the found path, excluding duplicate start
                current_pos = curr
                found = True
                break
            
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_pos = (curr[0] + dx, curr[1] + dy)
                if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and maze[new_pos[0]][new_pos[1]] == 0:
                    if new_pos not in local_visited:
                        frontier.put((heuristic(new_pos, min(goals, key=lambda g: heuristic(new_pos, g))), new_pos, new_path))
    
    return path if goals == [] else "Not all goals reachable"
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

path = best_first_search(maze, start, goals)
print("Path covering all goals:", path)
