import sys

def main():
    elf_calories = []
    elf_sum = 0
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            elf_calories.append(elf_sum)
            elf_sum = 0
        else:
            elf_sum += int(line)
    elf_calories.append(elf_sum)

    print(f"The maximum calories being carried is {max(elf_calories)}")

    top_three_sum = 0
    for i in range(3):
        top_three_sum += max(elf_calories)
        elf_calories.remove(max(elf_calories))

    print(f"The top three Elves carrying the most calories carry a total of {top_three_sum} calories.")


if __name__ == '__main__':
    main()
