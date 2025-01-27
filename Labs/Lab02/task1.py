import random

class System :
    def __init__(self) :
        self.components = []
        self.vulnerabilities = []
        for component in range(0,9) :
            self.components.append(random.choice([0,1]))
    
    def state(self) :
        for iter,component in enumerate(self.components) :
            if not component :
                self.vulnerabilities.append(f"component {iter}")
        print(f"{self.vulnerabilities}\nThese components are vulnerable") if 0 in self.components else print("All Components Functional")
        
class Agent :
    def __init__(self, system) :
        self.system = system
        self.logs = []
    
    def patch(self) :
        self.system.components = [1 for component in self.system.components]
        print(f"{self.system.vulnerabilities}\n These components were vulnerable and have been patched")

    def search(self) :
        for component in self.system.components :
            if not component :
                self.logs.append("Warning. Component is vulnerable")
            else :
                self.logs.append("Success!")
        self.patch()

system = System()
agent = Agent(sys)
system.state()
agent.search()
system.state()