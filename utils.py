import numpy as np

def fetch_subgrids(grid):
    if np.shape(grid) != (9, 9):
        return
    
    subgrids = []

    for block_row in range(0, 9, 3):
        for block_col in range(0, 9, 3):

            subgrid = grid[block_row:block_row+3, block_col:block_col+3]
            subgrids.append(subgrid)

    return subgrids

def subgrid_to_array(subgrid):
    arr = []

    for i in range(len(subgrid)):
        for j in range(len(subgrid)):
            arr.append(subgrid[i][j])

    return arr

def array_to_subgrid(arr):
    return np.array(arr).reshape((3, 3))


def subgrids_to_grid(subgrids):
    grid = np.zeros((9, 9), dtype=int)
    idx = 0
    for block_row in range(0, 9, 3):
        for block_col in range(0, 9, 3):
            grid[block_row:block_row+3, block_col:block_col+3] = subgrids[idx]
            idx += 1
    return grid