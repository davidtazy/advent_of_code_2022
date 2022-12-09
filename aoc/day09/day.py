from typing import List, Tuple
from ..tool import tool


class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = ""

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"[{self.id}({self.x},{self.y})]"

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Position(x, y)

    def move(self, direction):
        self.x += direction.x
        self.y += direction.y

    def __hash__(self):
        return hash((self.x, self.y))

    def clone(self):
        return Position(self.x, self.y)

    def set_id(self, id: int):
        if id == 0:
            self.id = "H"
        self.id = str(id)


class Direction:

    @staticmethod
    def Up():
        return Position(0, -1)

    @staticmethod
    def Down():
        return Position(0, 1)

    @staticmethod
    def Left():
        return Position(-1, 0)

    @staticmethod
    def Right():
        return Position(1, 0)

    @staticmethod
    def Move(char):
        m = dict(U=Direction.Up, D=Direction.Down,
                 L=Direction.Left, R=Direction.Right)

        return m[char]()


class Head:

    def __init__(self):
        self.pos = Position(0, 0)
        self.tail = Position(0, 0)
        self.tail_positions = set()

    def move(self, char: str):
        direction = Direction.Move(char)
        self.pos.move(direction)
        self.move_tail()

    def move_tail(self):

        delta = self.pos - self.tail
        if delta == Position(2, 0):
            self.tail.move(Direction.Right())
        elif delta == Position(-2, 0):
            self.tail.move(Direction.Left())
        elif delta == Position(0, -2):
            self.tail.move(Direction.Up())
        elif delta == Position(0, 2):
            self.tail.move(Direction.Down())

        elif delta == Position(1, 2):
            self.tail.move(Direction.Down())
            self.tail.move(Direction.Right())
        elif delta == Position(-1, 2):
            self.tail.move(Direction.Down())
            self.tail.move(Direction.Left())

        elif delta == Position(1, -2):
            self.tail.move(Direction.Up())
            self.tail.move(Direction.Right())
        elif delta == Position(-1, -2):
            self.tail.move(Direction.Up())
            self.tail.move(Direction.Left())

        elif delta == Position(2, -1):
            self.tail.move(Direction.Up())
            self.tail.move(Direction.Right())
        elif delta == Position(2, 1):
            self.tail.move(Direction.Down())
            self.tail.move(Direction.Right())

        elif delta == Position(-2, -1):
            self.tail.move(Direction.Up())
            self.tail.move(Direction.Left())
        elif delta == Position(-2, 1):
            self.tail.move(Direction.Down())
            self.tail.move(Direction.Left())

        elif delta == Position(2, -2):
            self.tail.move(Direction.Right())
            self.tail.move(Direction.Up())

        elif delta == Position(-2, 2):
            self.tail.move(Direction.Left())
            self.tail.move(Direction.Down())

        elif delta == Position(2, 2):
            self.tail.move(Direction.Right())
            self.tail.move(Direction.Down())

        elif delta == Position(-2, -2):
            self.tail.move(Direction.Left())
            self.tail.move(Direction.Up())

        elif abs(delta.x) == 2 and abs(delta.y) == 2:
            raise ValueError(f"DIAG ERRORRRR{delta}")

        elif abs(delta.x) > 2 or abs(delta.y) > 2:
            raise ValueError(f"FAR ERRORRRR{delta}")

        self.tail_positions.add(self.tail.clone())


class Rope:
    def __init__(self, lenght):
        self.elements = []
        for id in range(lenght):
            tail = Head()
            tail.pos.set_id(id)
            self.elements.append(tail)
        self.elements[-1].tail.set_id(lenght)

    def move(self, char: str):

        self.elements[0].move(char)

        for index, element in enumerate(self.elements[1:]):
            prev = self.elements[index]
            element.pos.x = prev.tail.x
            element.pos.y = prev.tail.y
            element.move_tail()

    def at(self, p: Position):
        for element in self.elements:
            if p == element.pos:
                return element.pos.id
        if p == self.elements[-1].pos:
            return self.elements[-1].pos.id

        if p == Position(0, 0):
            return "s"

        return "."

    def print(self):
        grid = ""
        for row in range(-20, 5):
            for col in range(-5, 20):
                grid += self.at(Position(col, row))
            grid += "\n"
        print(grid)


def part1(dir: str, file: str) -> int:

    head = Head()

    lines = tool.read_dataset_lines(dir, file)

    for line in lines:
        dep, repeat = line.split()
        repeat = int(repeat)

        for _ in range(repeat):
            head.move(dep)

    return len(head.tail_positions)


def part2(dir: str, file: str) -> int:

    rope = Rope(9)

    lines = tool.read_dataset_lines(dir, file)

    for line in lines:
        dep, repeat = line.split()
        repeat = int(repeat)

        for _ in range(repeat):
            rope.move(dep)

    return len(rope.elements[-1].tail_positions)
