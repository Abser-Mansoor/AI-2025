import random

class System :
    def __init__(self) :
        self.components = []
        self.vulnerabilities = [[],[]] # First sub-list holds Low Vul components
        vulner_dict = {
            0 : "Safe",
            1 : "Low",
            2 : "High"
        }
        for component in range(0,9) :
            self.components.append(random.choice([0,1,2]))
    
    def state(self) :
        for iter,component in enumerate(self.components) :
            if component == 1 :
                self.vulnerabilities[0].append(f"component {iter}")
            if component == 2 :
                self.vulnerabilities[1].append(f"component {iter}")
        if (self.vulnerabilities[0] == [] and self.vulnerabilities[1] == []) :
            print("System is Safe")
        elif (self.vulnerabilities[0] != [] and self.vulnerabilities[1] != []) :
            print(f"These components are vulnerable to Low level attacks: {self.vulnerabilities[0]}\nThese components are vulnerable to High level attacks: {self.vulnerabilities[1]}")
        elif (self.vulnerabilities[0] != []) :
            print(f"These components are vulnerable to Low level attacks: {self.vulnerabilities[0]}")
        elif (self.vulnerabilities[1] != []) :
            print(f"These components are vulnerable to High level attacks: {self.vulnerabilities[1]}")
class Agent :
    def __init__(self, system: System) :
        self.system = system
        self.logs = []
    
    def patch(self) :
        self.system.components = [1 for component in self.system.components]
        print(f"{self.system.vulnerabilities[0]}: These components had low vulnerability and have been patched\n")
        self.system.vulnerabilities[0].clear()

    def search(self) :
        for component in self.system.components :
            if not component :
                self.logs.append("Warning. Component is vulnerable")
            else :
                self.logs.append("Success!")
        self.patch()

sys = System()
agent = Agent(sys)
sys.state()
agent.search()
sys.state()
