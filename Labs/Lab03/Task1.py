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
    
agent = Agent()
print(f"{agent.Depth_First_Search()}")
