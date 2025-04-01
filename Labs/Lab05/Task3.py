import random
import math

CITIES = ['Kalinin', 'Stalingrad', 'Moscow', 'Kiev', 'Mogilev', 'Dnieperpetrovsk', 'Leningrad', 'Rostov', 'Baku', 'Vladivostok']
CITIES_COORDS = { city: (random.randint(0,100), random.randint(0,100)) for city in CITIES}
POPULATION_SIZE = 100
GENERATIONS = 1000

def euclidean_dist(city1, city2) :
    return math.sqrt((CITIES_COORDS[city2][0] - CITIES_COORDS[city1][0]) ** 2 + (CITIES_COORDS[city2][1] - CITIES_COORDS[city1][1]) ** 2)

def generate_individual() :
    return random.sample(CITIES, len(CITIES))

# A greater decimal means a better solution
def fitness(individual) :
    return 1 / sum(euclidean_dist(individual[i], individual[i+1]) for i in range(len(individual)-1))

def tournament_selection(population) :
    tournament = random.sample(population, k=5)
    return max(tournament, key=fitness)

def ordered_crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[start:end] = parent1[start:end]
    remaining_cities = [city for city in parent2 if city not in child]
    child = [remaining_cities.pop(0) if city is None else city for city in child]
    return child

def swap_mutation(child, mutation_rate=0.3) :
    if random.random() < mutation_rate :
        idx1,idx2 = random.sample(range(len(child)),2)
        child[idx1], child[idx2] = child[idx2], child[idx1]
    return child

def genetic_algorithm_TSP() :
    population = [generate_individual() for _ in range(POPULATION_SIZE)]
    for generation in range(GENERATIONS) :
        new_pop = []
        for _ in range(POPULATION_SIZE // 2) :
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child1 = ordered_crossover(parent1, parent2)
            child2 = ordered_crossover(parent2, parent1)
            child1 = swap_mutation(child1)
            child2 = swap_mutation(child2)
            new_pop.append(child1)
            new_pop.append(child2)
        population = new_pop
    best_route = max(population, key=fitness)
    return best_route, fitness(best_route)

best_route, best_fitness = genetic_algorithm_TSP()
print(f"Best route: {best_route}")
print(f"Best fitness: {best_fitness}")
