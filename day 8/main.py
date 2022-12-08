import numpy as np


def calculate_sight(value, trees):
    sight = 1
    if not np.size(trees):
        return 0
    for tree in trees:
        if value > tree:
            sight += 1
        else:
            return min(len(trees), sight)
    return min(len(trees), sight)


def main():
    array = np.genfromtxt("input.txt", delimiter=1)
    visible_trees = np.empty(array.shape, dtype=str)
    sight_trees = np.empty(array.shape)

    # Part 1
    for _ in range(0, 4):
        for index_x, line in enumerate(array):
            highest = -1
            for index_y, tree in enumerate(line):
                if tree > highest:
                    highest = tree
                    visible_trees[index_x, index_y] = "x"
        array = np.rot90(array)
        visible_trees = np.rot90(visible_trees)
    print(np.count_nonzero(visible_trees == 'x'))

    # Part 2
    for index_x, line in enumerate(array):
        for index_y, tree in enumerate(line):
            right = calculate_sight(tree, line[index_y+1:])
            left = calculate_sight(tree, np.flip(line[:index_y]))
            down = calculate_sight(tree, array[index_x+1:, index_y])
            up = calculate_sight(tree, np.flip(array[:index_x, index_y]))

            score = up * left * down * right
            sight_trees[index_x, index_y] = score
    print(np.max(sight_trees))


main()
