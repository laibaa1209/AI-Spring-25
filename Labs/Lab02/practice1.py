class Enviroment:
    def __init__(self, state):
        self.state = state

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = "cleaned"

class SimpleReflexAgent:
    def __init__(self):
        pass

    def act(self, percept):
        return "clean the room" if percept == "dirty"  else "room is already cleaned"  

def runAgent(agent, enviroment, steps):
    for step in range (steps):
        percept = enviroment.get_percept()
        action = agent.act(percept)

        print(f"step- {steps}, percept- {percept}, action- {action}")
        if percept == "dirty":
            enviroment.clean_room()

def main():
    states = ["dirty", "clean", "dirty", "clean", "clean", "dirty"]
    
    agent = SimpleReflexAgent()
    enviroment = Enviroment("dirty")

    runAgent(agent, enviroment, states)

main()