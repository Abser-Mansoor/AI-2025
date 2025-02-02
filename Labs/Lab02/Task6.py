import numpy as np

class Agent:
    def __init__(self):
        self.grid = {
            'a': '.', 'b': '.', 'c': '!', 
            'd': '.', 'e': '!', 'f': '.', 
            'g': '.', 'h': '.', 'i': '!'
        }
        self.loc = 'a'

    def printgrid(self):
        grid_layout = [['a', 'b', 'c'], 
                       ['d', 'e', 'f'], 
                       ['g', 'h', 'i']]
        
        for row in grid_layout:
            print(" ".join(self.grid[cell] for cell in row))
        print("---------")  # Horizontal separator

    def Action(self):
        path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']  
        for i in range(len(path)):
            self.printgrid()
            print(f"\nRobot is in room {self.loc}")

            if self.grid[self.loc] == '!':
                print("Fire Detected! Clearing....")
                self.grid[self.loc] = '.'
            if i == len(path)-1 : break
            self.loc = path[i + 1]  # Move to next room

        # Final state of the grid after all actions
        self.printgrid()
        print("\nFirefighting Complete!")

# Run the agent
agent = Agent()
agent.Action()
