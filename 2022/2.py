import sys

shapes = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors',
}

needed_outcome = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
}

shape_points = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3,
}

outcome_points = {
    'lose': 0,
    'draw': 3,
    'win':  6,
}


def outcome_for_player(choice_opponent, choice_player):
    if choice_opponent == choice_player:
        return 'draw'
    elif choice_opponent == 'Rock' and choice_player == 'Paper' \
         or choice_opponent == 'Paper' and choice_player == 'Scissors' \
         or choice_opponent == 'Scissors' and choice_player == 'Rock':
        return 'win'
    else:
        return 'lose'


def player_choice_for_outcome(choice_opponent, necessary_outcome):
    if necessary_outcome == 'draw':
        return choice_opponent
    elif necessary_outcome == 'win':
        if choice_opponent == 'Rock':
            return 'Paper'
        elif choice_opponent == 'Paper':
            return 'Scissors'
        elif choice_opponent == 'Scissors':
            return 'Rock'
    else:
        if choice_opponent == 'Rock':
            return 'Scissors'
        elif choice_opponent == 'Paper':
            return 'Rock'
        elif choice_opponent == 'Scissors':
            return 'Paper'


def part1(puzzle_input):
    total_score = 0
    for choices in puzzle_input:
        (opponent, player) = choices
        opponent = shapes[opponent]
        player = shapes[player]
        total_score += shape_points[player] \
            + outcome_points[outcome_for_player(opponent, player)]
    print(f'Total score part 1: {total_score}')

def part2(puzzle_input):
    total_score = 0
    for choices in puzzle_input:
        (opponent, outcome) = choices
        opponent = shapes[opponent]
        outcome = needed_outcome[outcome]
        total_score += shape_points[player_choice_for_outcome(opponent, outcome)] \
            + outcome_points[outcome]
    print(f'Total score part 2: {total_score}')

def main():
    puzzle_input = []
    for line in sys.stdin:
        puzzle_input.append(line.strip().split())
    part1(puzzle_input)
    part2(puzzle_input)


if __name__ == '__main__':
    main()
