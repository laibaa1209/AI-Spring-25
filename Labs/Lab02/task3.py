import random
class Environemnt:
    def __init__(self):
        self.backup_status = {f"Backup {i}" : random.choice(["Completed", "Failed"]) for i in range (6)}

    def get_status(self, backup_num):
        return self.backup_status[backup_num]
    
    def change_staus(self, backup_no):
        self.backup_status[backup_no] = "Retired"
        
class BackupAgent:
    def __init__(self):
        pass

    def action(self, status, backup_no):
        if status == "Failed":
            return f"{backup_no} is retired!\n"
        else:
            return "No action required"
        
def agent_run(env, agent):
    print("Scanning for Backups\n")
    for backup in env.backup_status.keys():
        status = env.get_status(backup)
        action = agent.action(backup, status)

        if status == "Failed":
            env.backup_status[backup] = "Retired"
        print(f"{backup}: Initial status: {status} -> {env.backup_status[backup]} | Action: {action}")

        if status == "Failed":
            env.backup_status[backup] = "Retired"
        
    print("\nFinal Load Status:")
    for backup, status in env.backup_status.items():
        print(f"{backup}: {status}")

env = Environemnt()
agent = BackupAgent()

agent_run(env, agent)

