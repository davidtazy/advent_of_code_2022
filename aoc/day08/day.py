from typing import List, Tuple
from ..tool import tool


def get_grid(dir: str, file: str) -> int:
    lines = tool.read_dataset_lines(dir, file)
    ret = []
    for line in lines:
        row = []
        for e in line:
            row.append(int(e))
        ret.append(row)
    return ret


def grid_size(grid):
    width = len(grid[0])
    height = len(grid)

    return width, height


def is_on_edge(grid, col, row):
    if col == 0 or row == 0:
        return True

    width, height = grid_size(grid)

    if col >= width - 1:
        return True
    if row >= height - 1:
        return True

    return False


def get_cross_trees(grid, col, row):

    width, height = grid_size(grid)
    ret = []
    for c in range(width):
        if c != col:
            ret.append((c, row))

    for r in range(height):
        if r != row:
            ret.append((col, r))

    return ret


def get_top_trees(grid, col, row):
    ret = []
    for r in reversed(range(row)):
        ret.append((col, r))
    return ret


def get_left_trees(grid, col, row):
    ret = []
    for c in reversed(range(col)):
        ret.append((c, row))
    return ret


def get_bottom_trees(grid, col, row):
    _, height = grid_size(grid)
    ret = []
    for r in range(row+1, height):
        ret.append((col, r))
    return ret


def get_right_trees(grid, col, row):
    width, _ = grid_size(grid)
    ret = []
    for c in range(col+1, width):
        ret.append((c, row))
    return ret


def all_trees(grid):
    width, height = grid_size(grid)
    ret = []
    for c in range(width):
        for r in range(height):
            ret.append((c, r))
    return ret


def height_of(grid, col, row):
    return grid[row][col]


def is_visible(tree_height, grid, view):
    return all(map(lambda pos: tree_height > height_of(
        grid, *pos), view))


def part1(dir: str, file: str) -> int:

    grid = get_grid(dir, file)
    count = 0
    for (c, r) in all_trees(grid):

        if is_on_edge(grid, c, r):
            count += 1
        else:
            tree_height = grid[r][c]
            if any([
               is_visible(tree_height, grid, get_bottom_trees(grid, c, r)),
               is_visible(tree_height, grid, get_top_trees(grid, c, r)),
               is_visible(tree_height, grid, get_left_trees(grid, c, r)),
               is_visible(tree_height, grid, get_right_trees(grid, c, r))
               ]) is True:
                count += 1

    return count


def multiply(list):
    ret = 1
    for e in list:
        ret *= e
    return ret


def count_visible(tree_height, grid, view):
    count = 0

    height_view = list(map(lambda pos: height_of(grid, *pos), view))

    for height in height_view:
        count += 1
        if tree_height <= height:
            break
    return count


def part2(dir: str, file: str) -> int:

    grid = get_grid(dir, file)
    best_view = 0

    for (c, r) in all_trees(grid):

        if not is_on_edge(grid, c, r):

            tree_height = grid[r][c]
            view = multiply([
                count_visible(tree_height, grid, get_bottom_trees(grid, c, r)),
                count_visible(tree_height, grid, get_top_trees(grid, c, r)),
                count_visible(tree_height, grid, get_left_trees(grid, c, r)),
                count_visible(tree_height, grid, get_right_trees(grid, c, r))
            ])
            best_view = max(view, best_view)

    return best_view
