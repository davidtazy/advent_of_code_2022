from aoc.day04.day import part1,  part2, get_inputs, contains, overlap

DATASET = "test/data/day04.bin"


def test_get_inputs(root_dir):
    assert get_inputs(root_dir, DATASET) == [
        [2, 4, 6, 8],
        [2, 3, 4, 5],
        [5, 7, 7, 9],
        [2, 8, 3, 7],
        [6, 6, 4, 6],
        [2, 6, 4, 8],
    ]


def test_contains():
    assert contains([2, 4, 6, 8]) is False
    assert contains([2, 3, 4, 5]) is False
    assert contains([5, 7, 7, 9]) is False
    assert contains([2, 8, 3, 7]) is True
    assert contains([6, 6, 4, 6]) is True
    assert contains([2, 6, 4, 8]) is False


def test_overlap():
    assert overlap([2, 4, 6, 8]) is False
    assert overlap([2, 3, 4, 5]) is False
    assert overlap([5, 7, 7, 9]) is True
    assert overlap([2, 8, 3, 7]) is True
    assert overlap([6, 6, 4, 6]) is True
    assert overlap([2, 6, 4, 8]) is True


def test_part1(root_dir):
    assert part1(root_dir, DATASET) == 2


def test_part2(root_dir):
    assert part2(root_dir, DATASET) == 4
