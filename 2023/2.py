from typing import Dict, List

from aoc_utils import read_stdin

limits = {"red": 12, "green": 13, "blue": 14}


def main():
    data = read_stdin()
    print(f"{sum(part1(data))=}")
    print(f"{sum(part2(data))=}")


def parse_game(game: str) -> List[tuple[int, str]]:
    return [
        game_set.split(",")
        for game_set in [game_set.strip() for game_set in game.split(";")]
    ]


def parse_set(set_txts: List[str]) -> tuple[int, str]:
    return [(int(pick.split()[0]), pick.split()[1]) for pick in set_txts]


def part1(data: List[str]) -> List[int]:
    def is_game_possible(game_txt: str) -> bool:
        return all(
            [
                all(
                    (False if (num > limits[color]) else True)
                    for num, color in parse_set(s)
                )
                for s in parse_game(game_txt)
            ]
        )

    def g(data: List[str]) -> List[int]:
        ids = list(map(lambda x: int(x.split(":")[0].split()[1]), data))
        games = list(map(lambda x: x.split(":")[1].strip(), data))
        return [
            id
            for id, _ in filter(
                lambda x: is_game_possible(x[1]), zip(ids, games)
            )
        ]

    return g(data)


def part2(data: List[str]) -> List[int]:
    def power(game_txt: str) -> Dict[str, int]:
        sets = [parse_set(s) for s in parse_game(game_txt)]
        rgb_max = {"red": 0, "green": 0, "blue": 0}
        for s in sets:
            for num, color in s:
                if num > rgb_max[color]:
                    rgb_max[color] = num
        return rgb_max["red"] * rgb_max["green"] * rgb_max["blue"]

    return [power(game.split(":")[1].strip()) for game in data]


if __name__ == "__main__":
    main()
