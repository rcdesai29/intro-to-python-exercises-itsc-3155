row = int(input("Enter row number (1-5): "))
column = int(input("Enter column number (1-5): "))

grid = []
for i in range(5):
    grid.append(["0"] * 5)

for i in range(5):
    grid[row - 1][i] = "1"
    grid[i][column - 1] = "1"

for line in grid:
    print(" ".join(line))
