from collections import deque

class BidirectionalSearch:
    def __init__(self, start, goal):
        self.graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B', 'H'],
        'E': ['B', 'I'],
        'F': ['C'],
        'G': ['C', 'J'],
        'H': ['D'],
        'I': ['E'],
        'J': ['G']
    }

        self.start = start
        self.goal = goal

    def search(self):
        forward_queue = deque([(self.start, [self.start])])
        backward_queue = deque([(self.goal, [self.goal])])
        forward_visited = {}
        backward_visited = {}

        while forward_queue and backward_queue:
            
            f_node, f_path = forward_queue.popleft()
            forward_visited[f_node] = f_path
            for neighbor in self.graph.get(f_node, []):
                if neighbor in backward_visited:
                    return f_path + backward_visited[neighbor][::-1]
                forward_queue.append((neighbor, f_path + [neighbor]))

            b_node, b_path = backward_queue.popleft()
            backward_visited[b_node] = b_path
            for neighbor in self.graph.get(b_node, []):
                if neighbor in forward_visited:
                    return forward_visited[neighbor] + b_path[::-1]
                backward_queue.append((neighbor, b_path + [neighbor]))

        return None

class IDDFS:
    def __init__(self, start, goal):
        self.graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': ['H'],
        'E': [],
        'F': ['I'],
        'G': [],
        'H': [],
        'I': []
        }
        self.start = start
        self.goal = goal

    def dls(self, node, path, depth):
        if depth == 0:
            return None if node != self.goal else path
        for neighbor in self.graph.get(node, []):
            result = self.dls(neighbor, path + [neighbor], depth - 1)
            if result:
                return result
        return None

    def search(self):
        depth = 0
        while True:
            result = self.dls(self.start, [self.start], depth)
            if result:
                return result
            depth += 1

agent = IDDFS('A', 'E')
print("IDDFS Path:", agent.search())
agent = BidirectionalSearch('A', 'I')
print("Bidirectional Search Path:", agent.search())
