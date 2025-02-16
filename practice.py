from queue import PriorityQueue

def Best_First_Search(start, goal, graph) :
    # Create a priority queue to hold the nodes to be visited
    pq = PriorityQueue()
    path = [start]
    pq.put((0, start)) # First Value is the priority so Heuristic becomes the priority
    visited = set()
    while not pq.empty() :
        curr_cost, curr_node = pq.get()
        visited.add(curr_node)
        if curr_node == goal:
            return f" Path found: {path}"
        for neighbour, cost in graph[curr_node] :
            if neighbour not in visited :
                pq.put((cost, neighbour))
                path += neighbour
    return "Goal is unreachable"

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0 # Cost from start node to curr_node
        self.h = 0 # heuristic estimate of the cost from curr_node to end node
        self.f = 0 # total cost
    
    def __lt__(self, other) :
        return self.f < other.f
def heuristic(current_pos, end_pos) :
    # Manhattan distance heuristic
    return abs(current_pos[0] - end_pos[0]) + abs(current_pos[1] - end_pos[1])

def Maze_Best_First_Search(maze, start, end) :
    rows, cols = len(maze), len(maze[0])
    start_node = Node(start)
    end_node = Node(end)
    frontier = PriorityQueue()
    frontier.put(start_node)
    visited = set()

    while not frontier.empty() :
        curr_node = frontier.get()
        curr_pos = curr_node.position

        if curr_node.position == end :
            path = []
            while curr_node:
                path.append(curr_node.position)
                curr_node = curr_node.parent
            return f"Path Found {path[::-1]}"
        
        visited.add(curr_pos)
        for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)] :
            new_pos = (curr_pos[0] + dx, curr_pos[1] + dy)
            if (0 <= new_pos[0] < rows) and (0 <= new_pos[1] < cols) and maze[new_pos[0]][new_pos[1]] == 0 and new_pos not in visited :
                new_node = Node(new_pos, curr_node)
                new_node.g = curr_node.g + 1
                new_node.h = heuristic(new_pos, end)
                new_node.f = new_node.h
                frontier.put(new_node)
                visited.add(new_pos)
    return "Path Not Found"

def Astar_Search(graph, start, goal) :
    visited = set()
    pq = PriorityQueue()
    pq.put((0,start))
    path = []
    while not pq.empty():
        curr_cost, curr_node = pq.get()
        if curr_node not in visited :
            visited.add(curr_node)
            path += curr_node
            if curr_node == goal:
                return f"Path Found: {path}"
            for node, cost, heur in graph[curr_node] :
                if node not in visited :
                    f_value = cost + heur + curr_cost
                    pq.put((f_value, node))
    return "Path not Found"

Astar_graph = {
'A': [('B', 5, 9), ('C', 8, 5)], # (neighbor, cost, heuristic)
'B': [('D', 10, 4)], # (neighbor, cost, heuristic)
'C': [('E', 3, 7)], # (neighbor, cost, heuristic)
'D': [('F', 7, 5)], # (neighbor, cost, heuristic)
'E': [('F', 2, 1)], # (neighbor, cost, heuristic)
'F': [] # (neighbor, cost, heuristic)
}
graph = {
'A': [('B', 5), ('C', 8)],
'B': [('D', 10)],
'C': [('E', 3)],
'D': [('F', 7)],
'E': [('F', 2)],
'F': []
}
maze = [
[0, 0, 1, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 1, 0, 1],
[0, 0, 1, 0, 0],
[0, 0, 0, 1, 0]
]
start = (0, 0)
end = (4, 4)
print(Best_First_Search('A', 'F', graph)) # This will return the shortest path from A to F
print(Maze_Best_First_Search(maze,start,end))
print(Astar_Search(Astar_graph, 'A', 'F')) # This will return the shortest path from A to F
