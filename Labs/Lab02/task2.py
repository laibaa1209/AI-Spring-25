import random

class System :
    def __init__(self):
        self.servers = []
        loads_dictionary = {
            0 : "Underloaded",
            1 : "Balanced",
            2 : "Overloaded"
        }
        for _ in range(0,5) :
            choice = random.choice([0,1,2])
            self.servers.append(loads_dictionary[choice])
    
    def status(self) : 
        for iter in range(len(self.servers)) :
            print(f"Server {iter+1} status: {self.servers[iter]}")

class Load_Balancer_Agent :
    def __init__(self,system):
        self.system = system

    def balance_servers(self) :
        print("\nBalancing Servers\n")
        for iter,server in enumerate(self.system.servers) :
            if server == "Overloaded" and "Underloaded" in self.system.servers :
                self.system.servers[iter] = "Balanced"
                self.system.servers[self.system.servers.index("Underloaded")] = "Balanced"

system = System()
agent = Load_Balancer_Agent(system)
system.status()
agent.balance_servers()
system.status()