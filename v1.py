
# create a 3x3 grid
grid = []
for i in range(3):
    row = []
    for j in range(3):
        row.append("-")
    grid.append(row)

# function to print the grid


def print_grid():
    for row in grid:
        print(" ".join(row))


def check_winner(player):
    # check rows
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] == player:
            return True
        if grid[0][i] == grid[1][i] == grid[2][i] == player:
            return True
    # check diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] == player:
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] == player:
        return True
    return False

# check for draw


def check_draw():
    for row in grid:
        if "-" in row:
            return False
    return True

# get row and col from position


def get_row_col(position):
    if position == 1:
        return 0, 0
    if position == 2:
        return 0, 1
    if position == 3:
        return 0, 2
    if position == 4:
        return 1, 0
    if position == 5:
        return 1, 1
    if position == 6:
        return 1, 2
    if position == 7:
        return 2, 0
    if position == 8:
        return 2, 1
    if position == 9:
        return 2, 2


player = "X"

while True:
    # print the grid
    print_grid()

    # get player input
    print(f"Player {player}'s turn")

    position = input("Enter position (between 1 and 9): ")

    row, col = get_row_col(int(position))

    # check if position not already taken
    if grid[row][col] != "-":
        print("Position already taken")
        continue

    # update the grid
    grid[row][col] = player

    # check for winner
    if check_winner(player):
        print(f"Player {player} wins!")
        print_grid()
        break

    # check for draw
    if check_draw():
        print("It's a draw!")
        print_grid()
        break

    # switch player
    if player == "X":
        player = "O"
    else:
        player = "X"
