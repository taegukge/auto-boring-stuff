### Character Picture Grid ###

grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]


for j in range(len(grid[0])):
    for i in range(len(grid)):
        print(grid[i][j], end='')   # within grid, list i element j; end=no spaces
    print()    # creates new line per list i (but why?)
