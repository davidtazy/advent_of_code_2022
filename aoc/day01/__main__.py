from .day01 import answer_of_the_day, part2

if __name__ == "__main__":

    elve, calories = answer_of_the_day(".", "dataset/day01.bin")
    print(f"day 1 part 1")
    print(f"day 1 part 1\nThe Elf carrying the most Calories:{elve}")
    print(f"How many total Calories is that Elf carrying? {calories}\n")

    print(
        "Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?"
    )
    print(part2(".", "dataset/day01.bin"))
