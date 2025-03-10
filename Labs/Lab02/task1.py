import random

class Environment:
    def __init__(self):
        self.component = {chr(65 + i): random.choice(["safe", "vulnerable"]) for i in range(9)}

    def get_percept(self, component_no):
        return self.component[component_no]

    def print_components(self, title):
        print(f"\n{title}")
        for comp, state in self.component.items():
            print(f"Component {comp}: {state}")
        print("-" * 30)

    def change_state(self, comp):
        self.component[comp] = "safe" 

class SecurityAgent:
    def __init__(self):
        self.patch_list = []  

    def scan(self, env):
        print("\n**System Scan:**")
        for comp in env.component.keys():
            state = env.get_percept(comp)
            if state == "vulnerable":
                print(f"Warning! Component {comp} is vulnerable. Added to patch list.")
                self.patch_list.append(comp)
            else:
                print(f"Component {comp} is secure.")

    def patching(self, env):
        print("\n**Patching Vulnerabilities:**")
        for comp in self.patch_list:
            env.change_state(comp)
            print(f"Component {comp} has been patched.")
        print("\nAll vulnerabilities have been fixed!")



env = Environment()
agent = SecurityAgent()

env.print_components("**Initial System Check:**")

agent.scan(env)
agent.patching(env)

env.print_components("**Final System Check:**")
