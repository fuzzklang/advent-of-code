import sys

def find_common_item(compartment1, compartment2):
    for character in compartment1:
        if character in compartment2:
            return character


def calculate_priority(item):
    if 'a' <= item <= 'z':
        return ord(item) - ord('a') + 1
    elif 'A' <= item <= 'Z':
        return ord(item) - ord('A') + 27


def part1(puzzle_input):
    priority_sum = 0
    for bag in puzzle_input:
        compartment1 = bag[:len(bag)//2]
        compartment2 = bag[len(bag)//2:]
        common_item = find_common_item(compartment1, compartment2)
        priority_sum += calculate_priority(common_item)
    print(f'Sum of priorities: {priority_sum}')


def part2(puzzle_input):
    

def main():
    puzzle_input = []
    for line in sys.stdin:
        puzzle_input.append(line.strip())
    part1(puzzle_input)


if __name__ == '__main__':
    main()
