import time

class Building:
    def __init__(self):
        self.grid = {
            'a': 'safe', 'b': 'safe', 'c': 'fire',
            'd': 'safe', 'e': 'fire', 'f': 'safe',
            'g': 'safe', 'h': 'safe', 'j': 'fire'
        }
        self.path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
        self.robot_position = 'a'
    
    def display_grid(self):
        visual_grid = [[' ' for _ in range(3)] for _ in range(3)]
        positions = list(self.grid.keys())
        
        for i in range(3):
            for j in range(3):
                room = positions[i * 3 + j]
                visual_grid[i][j] = '🔥' if self.grid[room] == 'fire' else ' '
        
        print("\nCurrent Building Status:")
        for row in visual_grid:
            print(" | ".join(row))
        print("\n" + "-" * 10)
    
    def move_robot(self):
        for room in self.path:
            self.robot_position = room
            print(f"Robot moved to room {room.upper()}.")
            
            if self.grid[room] == 'fire':
                print("🔥 Fire detected! Extinguishing...")
                self.grid[room] = 'safe'
                print("✅ Fire extinguished.")
            else:
                print("✅ Room is safe.")
            
            self.display_grid()
            time.sleep(5)  
        
        print("Robot has completed its task. All fires are extinguished!")

env = Building()

env.display_grid()

env.move_robot()
