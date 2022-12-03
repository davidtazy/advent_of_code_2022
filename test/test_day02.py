import aoc.tool.tool as tool
from aoc.day02.day import score, part1, fix_line, part2

DATASET = "test/data/day02.bin"


def test_can_read_game_input(root_dir):
    lines = tool.read_dataset_lines(root_dir, DATASET)
    assert len(lines) == 3


def test_score_round():

    assert score("A X") == 1 + 3
    assert score("A Y") == 2 + 6
    assert score("A Z") == 3 + 0

    assert score("B X") == 1 + 0
    assert score("B Y") == 2 + 3
    assert score("B Z") == 3 + 6

    assert score("C X") == 1 + 6
    assert score("C Y") == 2 + 0
    assert score("C Z") == 3 + 3


def test_part1(root_dir):
    assert part1(root_dir, DATASET) == 15


def test_fixline():

    assert fix_line("A X") == "A Z"
    assert fix_line("A Y") == "A X"
    assert fix_line("A Z") == "A Y"

    assert fix_line("B X") == "B X"
    assert fix_line("B Y") == "B Y"
    assert fix_line("B Z") == "B Z"

    assert fix_line("C X") == "C Y"
    assert fix_line("C Y") == "C Z"
    assert fix_line("C Z") == "C X"


def test_part2(root_dir):
    assert part2(root_dir, DATASET) == 12
