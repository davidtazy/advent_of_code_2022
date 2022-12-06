from typing import List, Tuple
from ..tool import tool


def get_inputs(dir: str, file: str) -> List[List[int]]:

    lines = tool.read_dataset_lines(dir, file)

    def to_arrays(line: str):
        line = line.replace("-", " ")
        line = line.replace(",", " ")
        line = line.split()
        return list(map(int, line))

    lines = map(to_arrays, lines)

    return list(lines)


def contains(line: List[int]) -> bool:
    assert len(line) == 4
    a = line[0:2]
    b = line[2:4]

    a = set(range(a[0], a[1] + 1))
    b = set(range(b[0], b[1] + 1))

    x = a.intersection(b)

    return x == a or x == b


def overlap(line: List[int]) -> bool:
    assert len(line) == 4
    a = line[0:2]
    b = line[2:4]

    a = set(range(a[0], a[1] + 1))
    b = set(range(b[0], b[1] + 1))

    x = a.intersection(b)

    return len(x) > 0


def part1(dir: str, file: str) -> int:

    lines = get_inputs(dir, file)

    lines = list(map(contains, lines))

    return lines.count(True)


def part2(dir: str, file: str) -> int:
    lines = get_inputs(dir, file)

    lines = list(map(overlap, lines))

    return lines.count(True)
