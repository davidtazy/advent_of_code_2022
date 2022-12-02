from typing import List, Tuple
from . import tool


def group(datas: str) -> List[str]:
    return datas.split("\n\n")


def sum_ints(datas: str) -> int:

    nums = datas.split("\n")
    nums = list(filter(lambda num: len(num) > 0, nums))
    return sum(list(map(lambda num: int(num), nums)))


def group_and_sum(datas: str) -> List[int]:

    return list(map(sum_ints, group(datas)))


def find_max(groups: List[int]) -> Tuple[int, int]:

    max_value = max(groups)
    index = groups.index(max_value)
    return index, max_value


def answer_of_the_day(dir, file) -> Tuple[int, int]:

    datas = tool.read_dataset(dir, file)
    groups = group_and_sum(datas)
    return find_max(groups)


def part2(dir, file) -> int:

    datas = tool.read_dataset(dir, file)
    groups = group_and_sum(datas)

    _, max_value = find_max(groups)
    sum = max_value
    groups.remove(max_value)

    _, max_value = find_max(groups)
    sum += max_value
    groups.remove(max_value)

    _, max_value = find_max(groups)
    sum += max_value
    groups.remove(max_value)

    return sum
