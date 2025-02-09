import heapq

class Agent() :
    def __init__(self) :
        self.tree = {
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
        self.goal = "G"
    
    def formulate_goal(self,goal) :
        if goal == self.goal :
            return "Found the Data"
        return "Searching"
    
    def Depth_First_Search(self) :
        visited = []
        stack = []

        stack.append('A')
        visited.append('A')
        while stack :
            curr_node = stack.pop()
            print(f"Visiting node {curr_node}")
            if curr_node == self.goal :
                return "Found The goal"
            for neighbour in reversed(self.tree[curr_node]) :
                if neighbour not in visited :
                    visited.append(neighbour)
                    stack.append(neighbour)
        return "Goal Not Found"
    
    def search(self, curr_node, path, depth, max_depth):
        if depth > max_depth:
            return None  # Reached depth limit
        print(f"Visiting node {curr_node}")
        if curr_node == self.goal:
            return path
        for neighbor in reversed(self.tree.get(curr_node, [])):
            result = self.search(neighbor, path + [neighbor], depth + 1, max_depth)
            if result:
                return result

        return None
    
    def Depth_Limited_Search(self) :
        return self.search('A', [], 0, 10)
    
class UCS_Agent:
    def __init__(self, start, goal):
        self.graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('D', 5), ('E', 1)],
        'C': [('F', 3), ('G', 7)],
        'D': [],
        'E': [],
        'F': [],
        'G': []
        }
        self.start = start
        self.goal = goal

    def search(self):
        pq = [(0, self.start, [self.start])]  # (cost, node, path)
        visited = set()

        while pq:
            cost, node, path = heapq.heappop(pq)

            if node in visited:
                continue

            if node == self.goal:
                return path, cost

            visited.add(node)
            for neighbor, weight in self.graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))

        return None

agent = Agent()
print(f"{agent.Depth_First_Search()}\n\n{agent.Depth_Limited_Search()}")
agent = UCS_Agent('A', 'F')
print("\nUCS Path and Cost:", agent.search())
