from aoc.day08.day import part1,  part2, get_grid, is_on_edge, get_top_trees, get_left_trees, get_bottom_trees, get_right_trees

DATASET = "test/data/day08.bin"


def test_get_grid(root_dir):
    grid = get_grid(root_dir, DATASET)

    assert len(grid) == 5
    assert grid[0] == [3, 0, 3, 7, 3]
    assert grid[-1] == [3, 5, 3, 9, 0]


def test_can_find_on_edge(root_dir):
    grid = get_grid(root_dir, DATASET)

    assert is_on_edge(grid, 0, 1) is True
    assert is_on_edge(grid, 1, 0) is True
    assert is_on_edge(grid, 4, 1) is True
    assert is_on_edge(grid, 1, 4) is True

    assert is_on_edge(grid, 2, 2) is False


def test_can_get_all_cross_tree_from_position(root_dir):
    grid = get_grid(root_dir, DATASET)

    assert get_top_trees(grid, 2, 2) == [(2, 1), (2, 0)]
    assert get_bottom_trees(grid, 2, 2) == [(2, 3), (2, 4)]

    assert get_left_trees(grid, 2, 2) == [(1, 2), (0, 2)]
    assert get_right_trees(grid, 2, 2) == [(3, 2), (4, 2)]


def test_part1(root_dir):
    assert part1(root_dir, DATASET) == 21


def test_part2(root_dir):
    assert part2(root_dir, DATASET) == 8
