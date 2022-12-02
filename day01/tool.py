import os


def read_dataset(dir: str, filename: str) -> str:

    file = os.path.join(dir, filename)

    if not os.path.exists(file):
        raise ValueError(f"{file} does not exists")

    with open(file, "r") as f:
        return f.read()
