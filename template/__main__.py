import sys
import os
from distutils.dir_util import copy_tree
import shutil

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

# copy day to module
copy_tree(source, destination)


def inject_day(file, day_str):
    assert os.path.exists(destination)
    content = ""
    with open(file, "r") as f:
        content = f.read()

    content = content.replace("dayXX", day_str)

    with open(file, "w") as f:
        f.write(content)


inject_day(os.path.join(destination, "__main__.py"), day_str)

# copy unit test

source = "template/template_test_day.py"
assert os.path.exists(source)

destination = f"test/test_{day_str}.py"
assert not os.path.exists(destination)

shutil.copyfile(source, destination)
inject_day(destination, day_str)


# create data file to receive exemple and dataset

with open(f"dataset/{day_str}.bin", 'w') as f:
    pass

with open(f"test/data/{day_str}.bin", 'w') as f:
    pass

# append test execution

with open("result.sh", "a+") as f:
    f.write(
        f"python -m aoc.{day_str}\n"
    )
