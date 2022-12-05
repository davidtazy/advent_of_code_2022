from aoc.day05.day import part1,  part2, get_crates, get_stacks_lines, get_moves, get_stacks, parse, move
from aoc.tool import tool

DATASET = "test/data/day05.bin"


def test_can_get_crates_by_line():
    assert get_crates("    [D]    ") == " D "
    assert get_crates("                [M]     [V]     [L]") == "    M V L"


def test_can_get_stacks_lines(root_dir):
    lines = tool.read_dataset_lines(root_dir, DATASET)
    assert get_stacks_lines(lines) == [" D ", "NC ", "ZMP"]


def test_can_get_stacks(root_dir):
    lines = [" D ", "NC ", "ZMP"]
    assert get_stacks(lines) == [["Z", "N"], ["M", "C", "D"], ["P"]]


def test_get_moves(root_dir):
    lines = tool.read_dataset_lines(root_dir, DATASET)
    assert get_moves(lines) == [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]


def test_parse(root_dir):
    stacks, moves = parse(root_dir, DATASET)
    assert moves == [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]
    assert stacks == [["Z", "N"], ["M", "C", "D"], ["P"]]


def test_move(root_dir):
    stacks, moves = parse(root_dir, DATASET)

    move(stacks, moves[0])
    assert stacks == [["Z", "N", "D"], ["M", "C"], ["P"]]

    move(stacks, moves[1])
    assert stacks == [[], ["M", "C"], ["P", "D", "N", "Z"]]

    move(stacks, moves[2])
    assert stacks == [["C", "M"], [], ["P", "D", "N", "Z"]]

    move(stacks, moves[3])
    assert stacks == [["C"], ["M"], ["P", "D", "N", "Z"]]


def test_part1(root_dir):
    assert part1(root_dir, DATASET) == "CMZ"


def test_part2(root_dir):
    assert part2(root_dir, DATASET) == "MCD"
