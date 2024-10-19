class TicTacToe:
    def __init__(self):
        self.grid = [["-" for _ in range(3)] for _ in range(3)]
        self.player = "X"

    def print_grid(self):
        for row in self.grid:
            print(" ".join(row))

    def check_winner(self, player):
        # Check rows and columns
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] == player:
                return True
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] == player:
                return True
        # Check diagonals
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == player:
            return True
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == player:
            return True
        return False

    def check_draw(self):
        for row in self.grid:
            if "-" in row:
                return False
        return True

    def get_row_col(self, position):
        mapping = {
            1: (0, 0), 2: (0, 1), 3: (0, 2),
            4: (1, 0), 5: (1, 1), 6: (1, 2),
            7: (2, 0), 8: (2, 1), 9: (2, 2)
        }
        return mapping.get(position, (None, None))

    def play(self):
        while True:
            self.print_grid()
            print(f"Player {self.player}'s turn")

            try:
                position = int(input("Enter position (between 1 and 9): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            row, col = self.get_row_col(position)

            if row is None or col is None:
                print("Invalid position. Choose a number between 1 and 9.")
                continue

            if self.grid[row][col] != "-":
                print("Position already taken")
                continue

            self.grid[row][col] = self.player

            if self.check_winner(self.player):
                self.print_grid()
                print(f"Player {self.player} wins!")
                break

            if self.check_draw():
                self.print_grid()
                print("It's a draw!")
                break

            self.player = "O" if self.player == "X" else "X"


# Initialize and start the game
game = TicTacToe()
game.play()
