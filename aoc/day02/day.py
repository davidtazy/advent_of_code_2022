from typing import List, Tuple
from ..tool import tool


VALUES = dict(A=1, B=2, C=3, X=1, Y=2, Z=3)


def is_draw(run: str) -> bool:
    return VALUES[run[0]] == VALUES[run[2]]


def has_won(run: str) -> bool:
    if VALUES[run[2]] == 3 and VALUES[run[0]] == 1:
        return False

    if VALUES[run[2]] == 1 and VALUES[run[0]] == 3:
        return True

    return VALUES[run[2]] > VALUES[run[0]]


def score(run: str) -> int:

    sc = VALUES[run[2]]

    if is_draw(run):
        return sc + 3

    if has_won(run):
        return sc + 6

    return sc


LOSE = dict(A="Z", B="X", C="Y")
DRAW = dict(A="X", B="Y", C="Z")
WIN = dict(A="Y", B="Z", C="X")


def fix_line(line: str) -> str:

    ret = line
    if line[2] == "X":
        # need to loose
        ret = ret.replace("X", LOSE[line[0]])

    if line[2] == "Y":
        # need to draw
        ret = ret.replace("Y", DRAW[line[0]])

    if line[2] == "Z":
        # need to win
        ret = ret.replace("Z", WIN[line[0]])

    return ret


def part1(dir: str, file: str) -> int:
    lines = tool.read_dataset_lines(dir, file)

    return sum(map(score, lines))


def part2(dir: str, file: str) -> int:
    lines = tool.read_dataset_lines(dir, file)

    lines = map(fix_line, lines)

    return sum(map(score, lines))
