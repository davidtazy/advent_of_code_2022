from typing import List, Tuple
from ..tool import tool


def get_duplicate(line: str) -> str:

    middle_index = len(line)//2
    first_half = set(line[:middle_index])
    second_half = set(line[middle_index:])

    return list(first_half.intersection(second_half))[0]


def get_priority(char: str) -> int:
    assert len(char) == 1
    assert char.isalpha()

    if char.islower():
        return 1 + ord(char) - ord("a")
    return 27 + ord(char) - ord("A")


def part1(dir: str, file: str) -> int:
    lines = tool.read_dataset_lines(dir, file)

    lines = map(get_duplicate, lines)
    lines = map(get_priority, lines)
    return sum(lines)


def get_dup3(lines: List[str]) -> str:
    assert len(lines) == 3

    lines = list(map(set, lines))

    ret = lines[0].intersection(lines[1])
    ret = ret.intersection(lines[2])

    return list(ret)[0]


def part2(dir: str, file: str) -> int:
    lines = tool.read_dataset_lines(dir, file)

    ret = []
    for index in range(0, len(lines), 3):

        lll = lines[index:index+3]
        ret.append(get_dup3(lll))

    ret = list(map(get_priority, ret))
    return sum(ret)
