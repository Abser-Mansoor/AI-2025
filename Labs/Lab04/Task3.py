from queue import PriorityQueue
import random
# Possibly faulty function
def greedy_best_first_delivery(graph, start, deliveries):
    pq = PriorityQueue()
    pq.put((0, start, []))  # (priority, current location, path)
    visited = set()
    path = []
    
    while not pq.empty():
        _, curr, curr_path = pq.get()
        if curr in visited:
            continue
        visited.add(curr)
        new_path = curr_path + [curr]
        
        if curr in deliveries:
            deliveries.remove(curr)
            path.extend(new_path[1:])  # Avoid duplicate starts
            if not deliveries:
                return path
            pq = PriorityQueue()  # Restart priority queue for next closest delivery
        
        for neighbor, cost in graph.get(curr, []):
            if neighbor not in visited:
                pq.put((cost, neighbor, new_path))
    
    return "Not all deliveries possible"

delivery_graph = {
    'A': [('B', 3), ('C', 5)],
    'B': [('D', 2), ('E', 4)],
    'C': [('E', 1), ('F', 7)],
    'D': [('G', 6)],
    'E': [('G', 3)],
    'F': [('G', 2)],
    'G': []
}
delivery_path = greedy_best_first_delivery(delivery_graph, 'A', {'D', 'E', 'G'})
print("Optimized Delivery Route:", delivery_path)
