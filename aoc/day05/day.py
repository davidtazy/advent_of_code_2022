from typing import List, Tuple
from ..tool import tool


def get_crates(line: str) -> str:
    return line[1 : len(line) : 4]


def get_stacks_lines(lines: List[str]):
    ret = []
    for line in lines:
        if line[1] == "1":
            break
        ret.append(get_crates(line))

    return ret


def get_stacks(lines: List[str]) -> List[List[str]]:

    stack_count = len(lines[0])
    stacks = [[] for _ in range(stack_count)]

    for line in reversed(lines):
        for index, char in enumerate(line):
            if char != " ":
                stacks[index].append(char)

    return stacks


def get_moves(lines: List[str]) -> List[int]:
    ret = []
    for line in lines:
        if len(line) == 0 or line[1] != "o":
            continue
        line = line.replace("move", "").replace("from", "").replace("to", "")
        ret.append(list(map(int, line.split())))
    return ret


def parse(dir: str, file: str):
    lines = tool.read_dataset_lines(dir, file)
    stack_lines = get_stacks_lines(lines)
    stacks = get_stacks(stack_lines)
    moves = get_moves(lines)
    return stacks, moves


def move(stacks, order):

    repeat = order[0]
    from_ = order[1] - 1
    to = order[2] - 1
    for _ in range(repeat):
        poped = stacks[from_].pop()
        stacks[to].append(poped)


def moveCrate9001(stacks, order):

    block_count = order[0]
    from_ = order[1] - 1
    to = order[2] - 1

    block = stacks[from_][-block_count:]
    del stacks[from_][-block_count:]
    stacks[to].extend(block)


def part1(dir: str, file: str) -> str:
    stacks, moves = parse(dir, file)
    for order in moves:
        move(stacks, order)

    ret = ""
    for stack in stacks:
        ret += stack.pop()

    return ret


def part2(dir: str, file: str) -> int:
    stacks, moves = parse(dir, file)
    for order in moves:
        moveCrate9001(stacks, order)

    ret = ""
    for stack in stacks:
        ret += stack.pop()

    return ret
