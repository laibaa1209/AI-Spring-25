import random

class Environment:
    def __init__(self):
        random.seed(42)  # Ensure the same results every time
        self.sys_vul = {f"Component {chr(65 + i)}": random.choice(["safe", "low risk vulnerable", "high risk vulnerable"]) for i in range(9)}

    def get_vulnerability(self, component):
        return self.sys_vul[component]
    
    def print_state(self):
        print("\nSystem State:")
        for component, vulnerability in self.sys_vul.items():
            print(f"Component: {component} | Vulnerability: {vulnerability}")
    
    def change_state(self, component):
        self.sys_vul[component] = "safe"


class SecurityAgent:
    def __init__(self):
        self.patch_list = []

    def action(self, vulnerability):
        if vulnerability == "low risk vulnerable":
            return "Warning!"
        elif vulnerability == "safe":
            return "Success!"
        
    def patching(self, env):
        print("\nPatching the components:")
        for comp in self.patch_list:
            env.change_state(comp)
            print(f"Patched: {comp}")
        print("All eligible components have been patched!!")

def run_agent(agent, env):
    print("\nScanning the system for vulnerabilities...\n")
    for comp in env.sys_vul.keys():
        vulnerability = env.get_vulnerability(comp)
        action = agent.action(vulnerability)
 
        print(f"Component: {comp} | Vulnerability: {vulnerability}")

        if vulnerability == "low risk vulnerable":
            agent.patch_list.append(comp)  # Append component to patch list
        elif vulnerability == "high risk vulnerable":
            print("Premium service required to patch this component.\n")
    
    agent.patching(env)
    env.print_state()  # Final system state after patching

env = Environment()
env.print_state()  

agent = SecurityAgent()
run_agent(agent, env)
