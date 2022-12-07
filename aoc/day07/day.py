from typing import List, Tuple, Dict
from ..tool import tool
from dataclasses import dataclass
from enum import Enum


class LineTYPE(Enum):
    CD = 1
    LS = 2
    OUT_DIR = 3
    OUT_FILE = 4


@dataclass
class Line:
    type: LineTYPE
    line: str
    size: int


@dataclass
class File:
    name: str
    size: int


class Directory:
    def __init__(self, name: str = "", parent=None):

        self.name: str = name
        self.size = -1
        self.parent = parent
        self.files: Dict[File] = {}
        self.dirs: Dict[Directory] = {}

    def debug_string(self):
        tree_str = f"dir {self.name} with {len(self.files)} files and {len(self.dirs)} sub_dirs\n"

        for folder in self.dirs.values():
            tree_str += folder.debug_string()

        return tree_str

    def cd(self, folder: str):
        if folder == "..":
            return self.parent
        return self.dirs[folder]

    def mkdir(self, folder: str):
        if self.dirs.get(folder, None) is None:
            self.dirs[folder] = Directory(folder, self)

    def touch(self, name: str, size: int):
        if self.files.get(name, None) is not None:
            raise ValueError(f"file {name} already exists")
        self.files[name] = File(name, size)

    def get_directory_size(self):

        if self.size >= 0:
            return self.size

        size = sum(map(lambda file: file.size, self.files.values()))

        for folder in self.dirs.values():
            size += folder.get_directory_size()

        self.size = size
        return size

    def get_all_dirs(self):
        dirs = [self]

        for folder in self.dirs.values():
            dirs.extend(folder.get_all_dirs())

        return dirs


def decode_line(line: str):

    if line.startswith("$ cd"):
        return Line(LineTYPE.CD, line.removeprefix("$ cd").strip(), 0)

    if line.startswith("$ ls"):
        return Line(LineTYPE.LS, "", 0)

    if line.startswith("dir"):
        return Line(LineTYPE.OUT_DIR, line.removeprefix("dir").strip(), 0)

    size, name = line.split()
    return Line(LineTYPE.OUT_FILE, name, int(size))


def decode_lines(lines):
    return list(map(decode_line, lines))


def load_directory(lines: List[Line]) -> Directory:
    ret = Directory()
    ret.name = lines[0].line
    lines = lines[1:]

    current_dir = ret

    for line in lines:
        if line.type == LineTYPE.LS:
            continue
        if line.type == LineTYPE.CD:
            current_dir = current_dir.cd(line.line)
        if line.type == LineTYPE.OUT_DIR:
            current_dir.mkdir(line.line)
        if line.type == LineTYPE.OUT_FILE:
            current_dir.touch(line.line, line.size)

    return ret


def part1(dir: str, file: str) -> int:

    lines = tool.read_dataset_lines(dir, file)
    lines = decode_lines(lines)
    dir_tree = load_directory(lines)

    dirs = dir_tree.get_all_dirs()

    dirs = filter(
        lambda d: d.get_directory_size() <= 100000,
        dirs
    )

    dirs = map(
        lambda d: d.get_directory_size(),
        dirs
    )

    return sum(dirs)


def part2(dir: str, file: str) -> int:

    lines = tool.read_dataset_lines(dir, file)
    lines = decode_lines(lines)
    root = load_directory(lines)

    dirs = root.get_all_dirs()

    dirs.sort(key=lambda d: d.get_directory_size())

    capacity = 70000000
    min_avail = 30000000
    used = root.get_directory_size()

    for fold in dirs:
        avail = capacity - used + fold.get_directory_size()
        if avail >= min_avail:
            return fold.get_directory_size()

    raise ValueError("day 7 part 2 not found")
