import random

class Environment:
    def __init__(self):
        random.seed(42)
        self.servers = {f"Server {i}": random.choice(["overloaded", "underloaded", "balanced"]) for i in range(5)}

    def get_percept(self, server):
        return self.servers[server]

    def change_overload_to_underload(self, server):
        self.servers[server] = "underloaded"

    def change_underload_to_balance(self, server):
        self.servers[server] = "balanced"

class LoadBalancerAgent:
    def __init__(self):
        pass

    def action(self, server, state, env):
        if state == "overloaded":
            env.change_overload_to_underload(server)
            return f"Moved load from {server} to another server."
        elif state == "underloaded":
            env.change_underload_to_balance(server)
            return f"{server} is now balanced."
        return f"{server} is already balanced."

    def agent_run(self, env):
        print("Scanning The Servers...\n")
        
        for server in env.servers.keys():
            state = env.get_percept(server)
            action_result = self.action(server, state, env)
            print(f"{server}: Initial state: {state} -> {env.servers[server]} | Action: {action_result}")
        
        print("\nFinal Load Status:")
        for server, state in env.servers.items():
            print(f"{server}: {state}")

env = Environment()
agent = LoadBalancerAgent()

agent.agent_run(env)
