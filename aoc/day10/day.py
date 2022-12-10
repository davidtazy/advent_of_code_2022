from typing import List, Tuple
from ..tool import tool
from dataclasses import dataclass, field


@dataclass
class Cpu:
    x: int = 1
    cycles: list = field(default_factory=lambda: [])

    def execute_cmd(self, cmd: str):
        if cmd == "noop":
            self.cycles.append(self.x)
            return self

        arg = int(cmd.split()[1])

        self.cycles.append(self.x)
        self.cycles.append(self.x)

        self.x += arg

        return self

    def draw_line(self):

        row = self.cycles[0:40]

        ret = ""

        for index, sprite in enumerate(row):
            if abs(index - sprite) < 2:
                ret += "#"
            else:
                ret += "."
        del self.cycles[0:40]
        return ret


def run_program(dir: str, file: str):
    lines = tool.read_dataset_lines(dir, file)

    cpu = Cpu()
    for cmd in lines:
        cpu.execute_cmd(cmd)

    return cpu


def part1(dir: str, file: str) -> int:
    cpu = run_program(dir, file)

    ret = 0
    for index in range(20, 221, 40):
        strength = cpu.cycles[index-1]*index
        ret += strength

    return ret


def part2(dir: str, file: str) -> str:

    cpu = run_program(dir, file)
    ret = ""

    for _ in range(6):
        ret += cpu.draw_line()
        ret += "\n"

    return ret
