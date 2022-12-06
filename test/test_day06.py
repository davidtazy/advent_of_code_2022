from aoc.day06.day import part1, part2, start_of_msg

DATASET = "test/data/day06.bin"


def test_find_start_of_msg():
    assert start_of_msg("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4) == 7
    assert start_of_msg("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5
    assert start_of_msg("nppdvjthqldpwncqszvftbrmjlhg", 4) == 6
    assert start_of_msg("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4) == 10
    assert start_of_msg("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4) == 11

    assert start_of_msg("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
    assert start_of_msg("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
    assert start_of_msg("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
    assert start_of_msg("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
    assert start_of_msg("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26


def test_part1(root_dir):
    assert part1(root_dir, DATASET) == 7


def test_part2(root_dir):
    assert part2(root_dir, DATASET) == 19
