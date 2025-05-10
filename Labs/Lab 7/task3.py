import random

GRID_SIZE = 10
SHIP_SIZES = [5, 4, 3, 3, 2]

class Board:
    def __init__(self):
        self.grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.ships = []

    def place_ship(self, size):
        while True:
            direction = random.choice(['H', 'V'])
            row = random.randint(0, GRID_SIZE - 1)
            col = random.randint(0, GRID_SIZE - 1)
            if self.valid_placement(row, col, size, direction):
                self.add_ship(row, col, size, direction)
                break

    def valid_placement(self, row, col, size, direction):
        if direction == 'H':
            if col + size > GRID_SIZE: return False
            return all(self.grid[row][c] == '.' for c in range(col, col + size))
        else:
            if row + size > GRID_SIZE: return False
            return all(self.grid[r][col] == '.' for r in range(row, row + size))

    def add_ship(self, row, col, size, direction):
        ship_coords = []
        for i in range(size):
            r, c = (row, col + i) if direction == 'H' else (row + i, col)
            self.grid[r][c] = 'S'
            ship_coords.append((r, c))
        self.ships.append(set(ship_coords))

    def receive_attack(self, row, col):
        if self.grid[row][col] == 'S':
            self.grid[row][col] = 'X'
            for ship in self.ships:
                ship.discard((row, col))
                if not ship:
                    self.ships.remove(ship)
                    return "Sunk!"
            return "Hit!"
        elif self.grid[row][col] == '.':
            self.grid[row][col] = 'O'
            return "Miss"
        return "Already tried"

    def all_sunk(self):
        return len(self.ships) == 0

def coord_input_to_index(coord):
    row = ord(coord[0].upper()) - ord('A')
    col = int(coord[1:]) - 1
    return row, col

def index_to_coord(row, col):
    return f"{chr(ord('A') + row)}{col + 1}"

def print_result(player, coord, result):
    print(f"{player} attacks: {coord} → {result}")

def main():
    player_board = Board()
    ai_board = Board()

    for size in SHIP_SIZES:
        player_board.place_ship(size)
        ai_board.place_ship(size)

    ai_targets = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE)]
    random.shuffle(ai_targets)
    last_hit = None

    while True:
        coord = input("Enter attack coordinate (e.g., B4): ").strip()
        try:
            r, c = coord_input_to_index(coord)
        except:
            print("Invalid coordinate.")
            continue
        result = ai_board.receive_attack(r, c)
        print_result("Player", coord.upper(), result)
        if ai_board.all_sunk():
            print("Player wins!")
            break

        # AI Turn
        if last_hit:
            r, c = last_hit
            possible = [(r+dr, c+dc) for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)] if 0<=r+dr<10 and 0<=c+dc<10]
            ai_targets = possible + ai_targets

        r, c = ai_targets.pop(0)
        result = player_board.receive_attack(r, c)
        print_result("AI", index_to_coord(r, c), result)
        if result == "Hit!":
            last_hit = (r, c)
        elif result == "Sunk!":
            last_hit = None

        if player_board.all_sunk():
            print("AI wins!")
            break

if __name__ == '__main__':
    main()
