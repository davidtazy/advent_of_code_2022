from aoc.day10.day import part1,  part2, Cpu, run_program

DATASET = "test/data/day10.bin"


def test_can_execute_nop_cmd():
    assert Cpu().execute_cmd("noop") == Cpu(x=1, cycles=[1])

    assert Cpu(x=5, cycles=[1]).execute_cmd("noop") == Cpu(x=5, cycles=[1, 5])


def test_can_execute_addx_cmd():
    assert Cpu().execute_cmd("addx 5") == Cpu(x=6, cycles=[1, 1])

    assert Cpu(x=4, cycles=[]).execute_cmd("addx -5"
                                           ) == Cpu(x=-1, cycles=[4, 4])


def test_run_program(root_dir):

    registers = run_program(root_dir, DATASET).cycles

    assert registers[20] == 21
    assert registers[60] == 19
    assert registers[100] == 18
    assert registers[140] == 21


def test_part1(root_dir):
    assert part1(root_dir, DATASET) == 13140


def test_draw_line(root_dir):
    cpu = run_program(root_dir, DATASET)
    assert cpu.draw_line() == "##..##..##..##..##..##..##..##..##..##.."
    assert cpu.draw_line() == "###...###...###...###...###...###...###."
    assert cpu.draw_line() == "####....####....####....####....####...."
    assert cpu.draw_line() == "#####.....#####.....#####.....#####....."
    assert cpu.draw_line() == "######......######......######......####"
    assert cpu.draw_line() == "#######.......#######.......#######....."


def test_part2(root_dir):
    assert part2(root_dir, DATASET) == """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""
