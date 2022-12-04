import sys
import os
from distutils.dir_util import copy_tree


# get day
print(sys.argv[1])
day = int(sys.argv[1])
assert day >= 1
assert day <= 25
day_str = f"day{day:02d}"
print(day_str)

assert os.path.exists(f"aoc")

source = f"template/day/"
assert os.path.exists(source)

destination = f"aoc/{day_str}"
assert not os.path.exists(destination)

#copy_tree(from_directory, to_directory)
# copy day to module
