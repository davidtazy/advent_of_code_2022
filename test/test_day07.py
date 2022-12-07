from aoc.day07.day import (
    part1,
    part2,
    decode_line,
    decode_lines,
    LineTYPE,
    Line,
    load_directory,
)
from aoc.tool import tool

DATASET = "test/data/day07.bin"


def test_decode_line():
    assert decode_line("$ cd /") == Line(LineTYPE.CD, "/", 0)
    assert decode_line("$ ls") == Line(LineTYPE.LS, "", 0)
    assert decode_line("dir q") == Line(LineTYPE.OUT_DIR, "q", 0)
    assert decode_line("8033020 d.log") == Line(LineTYPE.OUT_FILE, "d.log", 8033020)


def test_decode_lines(root_dir):
    lines = tool.read_dataset_lines(root_dir, DATASET)
    lines = decode_lines(lines)
    assert len(lines) == 23
    assert lines[0] == Line(LineTYPE.CD, "/", 0)
    assert lines[-1] == Line(LineTYPE.OUT_FILE, "k", 7214296)


def test_load_directory(root_dir):
    lines = tool.read_dataset_lines(root_dir, DATASET)
    lines = decode_lines(lines)
    dir_tree = load_directory(lines)

    tree_str = dir_tree.debug_string()
    print(tree_str)
    assert (
        tree_str
        == """dir / with 2 files and 2 sub_dirs
dir a with 3 files and 1 sub_dirs
dir e with 1 files and 0 sub_dirs
dir d with 4 files and 0 sub_dirs
"""
    )


def test_get_directory_size(root_dir):

    lines = tool.read_dataset_lines(root_dir, DATASET)
    lines = decode_lines(lines)
    dir_tree = load_directory(lines)

    assert dir_tree.get_directory_size() == 48381165


def test_get_all_dirs(root_dir):

    lines = tool.read_dataset_lines(root_dir, DATASET)
    lines = decode_lines(lines)
    dir_tree = load_directory(lines)

    assert len(dir_tree.get_all_dirs()) == 4


def test_part1(root_dir):
    assert part1(root_dir, DATASET) == 95437


def test_part2(root_dir):
    assert part2(root_dir, DATASET) == 24933642
