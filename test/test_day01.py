from day01.day01 import group, sum_ints, group_and_sum, find_max, answer_of_the_day, part2
from day01 import tool


DATASET = "test/data/day01.bin"


def test_can_read_dataset_from_file(root_dir):
    dataset = tool.read_dataset(root_dir, DATASET)
    assert type(dataset) == type("")
    assert len(dataset) == 54


def test_can_group_str(root_dir):
    dataset = tool.read_dataset(root_dir, DATASET)
    groups = group(dataset)
    assert len(groups) == 5


def test_can_sum_strings():
    inp = "1000\n2000\n"
    assert sum_ints(inp) == 3000


def test_group_and_sum():
    inp = "1000\n2000\n\n300"
    assert group_and_sum(inp) == [3000, 300]


def test_find_max():
    groups = [300, 3000]

    assert find_max(groups) == (1, 3000)


def test_answer_day(root_dir):

    assert answer_of_the_day(root_dir, DATASET) == (3, 24000)


def test_part2(root_dir):

    assert part2(root_dir, DATASET) == 45000
