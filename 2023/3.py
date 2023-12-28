import itertools
import operator
from typing import List

from aoc_utils import read_stdin


def group_numbers(lst: List[str]) -> List[tuple[int, int]]:
    ranges = []
    for _, g in itertools.groupby(enumerate(lst), lambda x: x[0] - x[1]):
        group = list(map(operator.itemgetter(1), g))
        ranges.append((group[0], group[-1]))
    return ranges


def is_range_neighbor_to_symbol(
    ran: tuple[int, int], scan_rows: List[str]
) -> bool:
    CMP_STRING = ".0123456789"

    start = max(ran[0] - 1, 0)
    end = min(ran[1] + 1, len(scan_rows[0]) - 1)

    if (scan_rows[1][start] not in CMP_STRING) or (
        scan_rows[1][end] not in CMP_STRING
    ):
        return True
    return any(
        map(
            lambda char: char not in CMP_STRING,
            "".join([row[start : end + 1] for row in scan_rows]),
        )
    )


def neighbor_rows(matrix: List[str], idx: int):
    EMPTY_STRING = "." * len(matrix[0])
    return [
        matrix[idx - 1] if idx >= 1 else EMPTY_STRING,
        matrix[idx],
        matrix[idx + 1] if idx < len(matrix) - 1 else EMPTY_STRING,
    ]


def get_digit_indices(data: List[str]) -> List[List[int]]:
    matrix = [list() for _ in range(len(data))]
    for row_idx, line in enumerate(data):
        for col_idx, char in enumerate(line):
            if char.isdigit():
                matrix[row_idx].append(col_idx)
    return matrix


def part1(data: List[str]) -> List[int]:
    indices = get_digit_indices(data)
    ranges_neighbor_to_symbol = {}
    for row_idx, lst in enumerate(indices):
        ranges = group_numbers(lst)
        scan_rows = neighbor_rows(data, row_idx)
        ranges_neighbor_to_symbol[row_idx] = list(
            filter(
                lambda ran: is_range_neighbor_to_symbol(ran, scan_rows),
                ranges,
            )
        )

    return [
        int(data[k][start : end + 1])
        for k, v in ranges_neighbor_to_symbol.items()
        for start, end in v
    ]


def all_gear_pos(data: List[str]):
    return [
        (col_idx, row_idx)
        for row_idx, s in enumerate(data)
        for col_idx, char in enumerate(s)
        if char == "*"
    ]


def ranges_adjacent_to_gear(
    ranges: List[List[tuple[int, int]]], gear_pos: tuple[int, int]
) -> List[tuple[int, int]]:
    adjacent_ranges = [list() for _ in ranges]
    col_idx, row_idx = gear_pos
    for idx_offset, row in enumerate(
        ranges[max(row_idx - 1, 0) : min(row_idx + 2, len(ranges))]
    ):
        for digit_start, digit_end in row:
            if digit_start - 1 <= col_idx <= digit_end + 1:
                adjacent_ranges[idx_offset + max(row_idx - 1, 0)].append(
                    (digit_start, digit_end)
                )
    return adjacent_ranges


def part2(data: List[str]) -> List[int]:
    digit_ranges = [group_numbers(lst) for lst in get_digit_indices(data)]
    adjacent_ranges_per_gear = [
        ranges_adjacent_to_gear(digit_ranges, gear_pos)
        for gear_pos in all_gear_pos(data)
    ]

    # Need to get correct row indices for ranges
    # and map ranges to actual integers
    valid_ranges = [
        lst
        for lst in adjacent_ranges_per_gear
        if sum([len(adjacent_ranges) for adjacent_ranges in lst]) == 2
    ]
    valid_ranges = [list(enumerate(lst)) for lst in valid_ranges]
    gear_ratios = []
    for adjacent_rng in valid_ranges:
        product = 1
        for row_idx, lst in adjacent_rng:
            for start, end in lst:
                num = int(data[row_idx][start : end + 1])
                product *= num
        gear_ratios.append(product)

    return gear_ratios


def main():
    data = read_stdin()

    print(sum(part1(data)))
    print(sum(part2(data)))


if __name__ == "__main__":
    main()
