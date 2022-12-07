from typing import List, Tuple
from ..tool import tool


def start_of_msg(msg: str, length: int) -> int:
    for index in range(len(msg) - length):
        sub = msg[index : index + length]
        if len(set(sub)) == length:
            return index + length
    raise ValueError(" start of msg not found")


def part1(dir: str, file: str) -> int:
    msg = tool.read_dataset(dir, file)
    return start_of_msg(msg, 4)


def part2(dir: str, file: str) -> int:
    msg = tool.read_dataset(dir, file)
    return start_of_msg(msg, 14)
