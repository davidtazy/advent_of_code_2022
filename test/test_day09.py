from aoc.day09.day import part1,  part2, Head, Position

DATASET = "test/data/day09.bin"

DATASET_2 = "test/data/day09_2.bin"


def test_can_move_head():

    head = Head()
    assert head.pos == Position(0, 0)

    head.move("U")
    assert head.pos == Position(0, -1)

    head.move("L")
    assert head.pos == Position(-1, -1)

    head.move("D")
    assert head.pos == Position(-1, 0)

    head.move("R")
    assert head.pos == Position(0, 0)


def test_dont_move_tail_when_touch_head():

    origin = Position(0, 0)

    head = Head()
    head.move("U")
    assert head.tail == origin

    head = Head()
    head.move("L")
    assert head.tail == origin

    head = Head()
    head.move("D")
    assert head.tail == origin

    head = Head()
    head.move("R")
    assert head.tail == origin

    head = Head()
    head.move("R")
    head.move("U")
    assert head.tail == origin

    head = Head()
    head.move("R")
    head.move("D")
    assert head.tail == origin

    head = Head()
    head.move("L")
    head.move("U")
    assert head.tail == origin

    head = Head()
    head.move("L")
    head.move("D")
    assert head.tail == origin


def test_tail_move_right():
    head = Head()
    head.move("R")
    head.move("R")
    assert head.tail == Position(1, 0)

    head = Head()
    head.move("R")
    head.move("U")
    head.move("R")
    assert head.tail == Position(1, -1)

    head = Head()
    head.move("R")
    head.move("D")
    head.move("R")
    assert head.tail == Position(1, 1)


def test_tail_move_left():
    head = Head()
    head.move("L")
    head.move("L")
    assert head.tail == Position(-1, 0)

    head = Head()
    head.move("L")
    head.move("U")
    head.move("L")
    assert head.tail == Position(-1, -1)

    head = Head()
    head.move("L")
    head.move("D")
    head.move("L")
    assert head.tail == Position(-1, 1)


def test_tail_move_up():
    head = Head()
    head.move("U")
    head.move("U")
    assert head.tail == Position(0, -1)

    head = Head()
    head.move("U")
    head.move("R")
    head.move("U")
    assert head.tail == Position(1, -1)

    head = Head()
    head.move("U")
    head.move("L")
    head.move("U")
    assert head.tail == Position(-1, -1)


def test_tail_move_down():
    head = Head()
    head.move("D")
    head.move("D")
    assert head.tail == Position(0, 1)

    head = Head()
    head.move("D")
    head.move("R")
    head.move("D")
    assert head.tail == Position(1, 1)

    head = Head()
    head.move("D")
    head.move("L")
    head.move("D")
    assert head.tail == Position(-1, 1)


def test_part1(root_dir):
    assert part1(root_dir, DATASET) == 13


def test_part2(root_dir):
    assert part2(root_dir, DATASET) == 1


def test_part2_2(root_dir):
    assert part2(root_dir, DATASET_2) == 36
