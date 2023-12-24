import re
from typing import List

from aoc_utils import read_stdin

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def main():
    data = read_stdin()

    calibration_values = part1(data)
    print(f"{sum(calibration_values)=}")

    new_calibration_values = part2(data)
    print(f"{sum(new_calibration_values)=}")


def part1(data: List[str]) -> List[int]:
    calibration_values = []
    for line in data:
        first = re.search("[0-9]", line)
        second = re.search("[0-9]", line[::-1])
        calibration_values.append(int(f"{first.group(0)}{second.group(0)}"))
    return calibration_values


def part2(data: List[str]) -> List[int]:
    calibration_values = []
    pattern = "|".join(numbers.keys()) + "|[0-9]"
    for line in data:
        matches = re.findall(rf"(?=({pattern}))", line)
        (first, second) = matches[0], matches[-1]
        if first in numbers:
            first = numbers[first]
        if second in numbers:
            second = numbers[second]
        val = int(f"{first}{second}")

        calibration_values.append(val)
    return calibration_values


if __name__ == "__main__":
    main()
