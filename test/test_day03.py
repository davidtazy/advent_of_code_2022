from aoc.day03.day import get_duplicate, get_priority, part1, get_dup3, part2

DATASET = "test/data/day03.bin"


def test_get_duplicate():
    assert get_duplicate("abcAbC") == "b"


def test_get_priority():
    assert get_priority("a") == 1
    assert get_priority("z") == 26

    assert get_priority("A") == 27
    assert get_priority("Z") == 52


def test_part1(root_dir):
    assert part1(root_dir, DATASET) == 157


def test_get_dup3():
    assert get_dup3(["abc", "bcd", "cde"]) == "c"


def test_part2(root_dir):
    assert part2(root_dir, DATASET) == 70
