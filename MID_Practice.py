from queue import PriorityQueue
from queue import Queue
import random as random

class Search_Agent:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.actions = {
            'up': (0, -1),
            'down': (0, 1),
            'left': (-1, 0),
            'right': (1, 0)
        }
    
    def Out_Of_Bounds(self, pos) :
        return pos[0] < 0 or pos[0] >= len(self.grid) or pos[1] < 0 or pos[1] >= len(self.grid[0])

    def get_neighbours(self, pos) :
        neighbours = []
        for action in self.actions :
            if self.Out_Of_Bounds(tuple(x + y for x, y in zip(pos, self.actions[action]))) :
                 continue
            else :
                neighbours.append(tuple(x + y for x, y in zip(pos, self.actions[action])))
        return neighbours

    def find_pos(self, node) :
        for row, r_val in enumerate(self.grid) :
            for cell, c_val in enumerate(self.grid[row]):
                if c_val == node :
                    return (row, cell)
        raise ValueError("Node does not exist in the grid")
    
    def DFS(self, curr_pos, visited, path) :
        if (self.grid[curr_pos[0]][curr_pos[1]] == 'T') :
            path.append(curr_pos)
            return True
        if curr_pos not in visited :
            visited.add(curr_pos)
            path.append(curr_pos)
            for neighbour in self.get_neighbours((curr_pos[0], curr_pos[1])) :
                if self.grid[neighbour[0]][neighbour[1]] == 'X':
                    continue
                if self.DFS(neighbour, visited, path) :
                    return True
        return False

    def init_DFS(self) :
        visited = set()
        path = []
        starting_positon = self.find_pos(self.start)
        return self.DFS(starting_positon, visited, path), path
    
    def BFS(self) :
        visited = set()
        visited.add(self.find_pos(self.start))
        queue = Queue()
        parent = {}
        queue.put(self.find_pos(self.start))
        while not queue.empty() :
            curr_pos = queue.get()
            if self.grid[curr_pos[0]][curr_pos[1]] == 'T':
                path = []
                while curr_pos is not None :
                    path.append(curr_pos)
                    curr_pos = parent.get(curr_pos)
                return path[::-1], True
            for neighbour in self.get_neighbours(curr_pos) :
                if neighbour in visited or self.grid[neighbour[0]][neighbour[1]] == 'X':
                    continue
                queue.put(neighbour)
                visited.add(neighbour)
                parent[neighbour] = curr_pos
        return None, False
grid = [
    ['O', 'O', 'X', 'O', 'T'], 
    ['O', 'X', 'O', 'O', 'X'],
    ['P', 'O', 'O', 'X', 'O'], 
    ['X', 'X', 'O', 'O', 'O'], 
    ['O', 'O', 'O', 'X', 'O']
]
agent = Search_Agent(grid, 'P', 'T')
path = agent.find_pos('P')
DFS_found, DFS_path = agent.init_DFS()
BFS_path, BFS_found = agent.BFS()
print(f"Path found by DFS: {bool(DFS_found)}\nPath: {DFS_path}\nPath found by BFS: {bool(BFS_found)}\nPath: {BFS_path}")

class A_Star :
    def __init__(self, grid, start, end) :
        self.grid = grid
        self.start = start
        self.end = end
        self.actions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        self.heuristic = lambda x, y: abs(x - (len(self.grid) - 1)) + abs(y - (len(self.grid[0]) - 1))

    def Out_Of_Bounds(self, pos) :
        return pos[0] < 0 or pos[0] >= len(self.grid) or pos[1] < 0 or pos[1] >= len(self.grid[0])
    
    def A_star(self) :
        pq = PriorityQueue()
        pq.put((0, self.start))
        g_cost = {self.start: 0}
        parent = {self.start: None}

        while not pq.empty() :
            curr_cost, curr_pos = pq.get()
            if curr_pos == self.end :
                path = []
                while curr_pos is not None :
                    path.append(curr_pos)
                    curr_pos = parent[curr_pos]
                return path[::-1], True, g_cost[self.end]
            x, y = curr_pos
            for action in self.actions :
                neighbour = (x + self.actions[action][0], y + self.actions[action][1])
                if not self.Out_Of_Bounds(neighbour) and self.grid[neighbour[0]][neighbour[1]] != '#':
                    new_g_cost = g_cost[curr_pos] + self.grid[neighbour[0]][neighbour[1]]
                    if neighbour not in g_cost or new_g_cost < g_cost[neighbour] :
                        g_cost[neighbour] = new_g_cost
                        priority = new_g_cost + self.heuristic(neighbour[0], neighbour[1])
                        pq.put((priority, neighbour))
                        parent[neighbour] = curr_pos
        return None, False, -1
    
grid = [
    [1, 2, 3, '#', 4],
    [1, '#', 1, 2, 2],
    [2, 3, 1, '#', 1],
    ['#', '#', 2, 1, 1],
    [1, 1, 2, 2, 1]
]
search = A_Star(grid, (0, 0), (4, 4))
A_star_path, A_star_found, A_star_cost = search.A_star()
print(f"A Star Found: {bool(A_star_found)}\nA Star Path: {A_star_path}\nA Star Cost: {A_star_cost}")

class Genetic_Algorithm :
    def __init__(self) :
        pass

    def function(self, x) :
        return 2 * (x*x) - 1
    
    def Binary_String_to_int(self, string) :
        return int(string, 2)
    
    def random_individual(self) :
        return ''.join([ random.choice('01') for _ in range(6) ]) # 6 bit string
    
    def fitness(self, individual) :
        return self.function(self.Binary_String_to_int(individual))
    
    def tourament_selection(self, population, k=3) :
        selected = random.sample(population, k)
        return max(selected, key=self.fitness)

    def uniform_crossover(self, parent1, parent2) :
        return ''.join(random.choice([p1,p2]) for p1, p2 in zip(parent1, parent2))
    
    def mutate(self, individual, generations, max_generations) :
        mutation_probability = 0.1 * (1 - generations/max_generations) # arbitrary probabilistic function
        return ''.join(str(1 - int(bit)) if random.random() < mutation_probability else bit for bit in individual)

    def genetic_algorithm(self, population_size=30, generations=100) :
        population = [ self.random_individual() for _ in range(population_size) ]
        fitness = [ self.fitness(individual) for individual in population ]
        
        for generation in range(generations) :
            new_pop = []
            for _ in range(population_size//2) :
                parent1 = self.tourament_selection(population)
                parent2 = self.tourament_selection(population)
                child1 = self.uniform_crossover(parent1, parent2)
                child2 = self.uniform_crossover(parent1, parent2)
                new_pop.append(self.mutate(child1, generation, generations))
                new_pop.append(self.mutate(child2, generation, generations))
            population = new_pop

        best_individual = sorted(population, key=self.fitness, reverse=True)[0]
        best_x = self.Binary_String_to_int(best_individual)
        return best_x, self.fitness(best_individual)

gen_algo = Genetic_Algorithm()
best_x, best_fitness = gen_algo.genetic_algorithm()
print(f"Best X: {best_x}, Best Fitness: {best_fitness}")
