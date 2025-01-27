import random

class Network :
    def __init__(self):
        self.tasks = []
        tasks_dictionary = {
            0 : "Completed",
            1 : "Failed",
        }
        for _ in range(0,5) :
            choice = random.choice([0,1])
            self.tasks.append(tasks_dictionary[choice])
    
    def status(self) : 
        for iter in range(len(self.tasks)) :
            print(f"Backup Task {iter+1} status: {self.tasks[iter]}")

class Backup_Management_Agent :
    def __init__(self,system):
        self.system = system

    def Retry_Failed_Tasks(self) :
        print("\nRetrying Failed Tasks\n")
        for iter,task in enumerate(self.system.tasks) :
            if task == "Failed" :
                seed = random.choice([0,1])
                while seed == 0 :
                    seed = random.choice([0,1])
                    # While loop simulates the random generation of string used for initialising the 
                    # tasks in Network class and the Failed task is updated only when the loop closes (seed becomes 1)
                self.system.tasks[iter] = "Completed"

system = Network()
agent = Backup_Management_Agent(system)
system.status()
agent.Retry_Failed_Tasks()
system.status()
