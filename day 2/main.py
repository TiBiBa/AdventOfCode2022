# A : Rock
# B : Paper
# C : Scissor

# X: Rock (1)
# Y: Paper (2)
# Z : Scissor (3)

# Lost: 0
# Draw: 3
# Won: 6

parse_dict = {'A': 'X', 'B': 'Y', 'C': 'Z'}
winner_dict = {'A': 'Y', 'B': 'Z', 'C': 'X'}
loser_dict = {'A': 'Z', 'B': 'X', 'C': 'Y'}
score_dict = {'X': 1, 'Y': 2, 'Z': 3}


def calculate_score(opponent, player):
    # Check for the draw
    if parse_dict.get(opponent) == player:
        return 3

    # Check for the win
    if opponent == "A" and player == "Y":
        return 6
    if opponent == "B" and player == "Z":
        return 6
    if opponent == "C" and player == "X":
        return 6

    # Otherwise, return 0
    return 0


def part1():
    with open("input.txt", mode="r", encoding="utf8") as file:
        content = file.read().splitlines()
        total_score = 0
        for strategy in content:
            opponent, player = strategy.split()
            total_score += calculate_score(opponent, player) + score_dict.get(player)
        print(total_score)


def get_move(opponent, conclusion):
    if conclusion == 'X':
        return loser_dict.get(opponent)
    if conclusion == 'Y':
        return parse_dict.get(opponent)
    return winner_dict.get(opponent)


def part2():
    with open("input.txt", mode="r", encoding="utf8") as file:
        content = file.read().splitlines()
        total_score = 0
        for strategy in content:
            opponent, conclusion = strategy.split()
            player = get_move(opponent, conclusion)
            print(player)
            total_score += calculate_score(opponent, player) + score_dict.get(player)
        print(total_score)


# part1()
part2()
