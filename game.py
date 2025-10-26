import random
import numpy as np
import utils


# Custom print
def display(grid):
    if(np.shape(grid) != ((9,9))): return

    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            if(grid[i][j] == 0): print(" ", end=" ")
            else: print(int(grid[i][j]), end=" ")

        print() 

    print()

def is_valid(grid, row, col, num):
    if num in grid[row]:
        return False
    
    if num in grid[:, col]:
        return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    if num in grid[start_row:start_row+3, start_col:start_col+3]:
        return False
    
    return True

# recursive backtracking algorithm by inside code on youtube
def fill_grid(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)
                for num in nums:
                    if is_valid(grid, i, j, num):
                        grid[i][j] = num
                        if fill_grid(grid):
                            return True
                        grid[i][j] = 0
                return False
    return True

def generate_sudoku():
    grid = np.zeros((9, 9), dtype=int)
    fill_grid(grid)
    return grid

# Hides x amount of squares depending on difficulty
# It is a bad solution in practice, as difficulty should be adapted
# to how humans solve the problems :)
def assign_difficulty(grid, difficulty):
    tiles_to_remove = 0
    match difficulty:
        case 0:
            tiles_to_remove = 2
        case 1:
            tiles_to_remove = 3
        case 2:
            tiles_to_remove = 4

    subgrids = utils.fetch_subgrids(grid)

    for idx, subgrid in enumerate(subgrids):
        flat = utils.subgrid_to_array(subgrid)
        selected = []

        for _ in range(tiles_to_remove):
            to_remove = random.randint(0, len(flat) - 1)
            while to_remove in selected:
                to_remove = random.randint(0, len(flat) - 1)
            flat[to_remove] = 0
            selected.append(to_remove)

        subgrids[idx] = utils.array_to_subgrid(flat)

    return utils.subgrids_to_grid(subgrids)


# Check if every row, column, and subgrid has every number 1-9
def is_solved(grid):
    if np.shape(grid) != (9, 9): return False

    if np.any(grid == 0): return False

    for row in grid:
        if set(row) != set(range(1, 10)):
            return False

    for col in grid.T:
        if set(col) != set(range(1, 10)):
            return False

    for block_row in range(0, 9, 3):
        for block_col in range(0, 9, 3):
            block = grid[block_row:block_row+3, block_col:block_col+3].flatten()
            if set(block) != set(range(1, 10)):
                return False

    return True

def is_filled(grid):
    return 0 not in grid

def remove(grid, i, j):
    grid[i][j] = 0;

def add(grid, number, i, j):
    grid[i][j] = number;
