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
        print(f"{self.components if self.components not in self.vulnerabilities[0][-1] and self.components not in self.vulnerabilities[1][-1] else None}\nThese components are functional\n\n{self.vulnerabilities[0]}\nThese components have low vulnerability\n\n{self.vulnerabilities[1] if self.vulnerabilities[1] else None}\nThese components have high vulnerability\n")
class Agent :
    def __init__(self, system) :
        self.system = system
        self.logs = []
    
    def patch(self) :
        self.system.components = [1 for component in self.system.components]
        print(f"{self.system.vulnerabilities[0]}\nThese components had low vulnerability and have been patched\n")

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
