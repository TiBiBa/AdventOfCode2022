import numpy as np


def main():
    # Keep track of a list of not-visible trees, also count all trees total
    # Walk from four directions

    visible_trees = []

    with open("test.txt", mode="r", encoding="utf8") as file:
        tree_lines = file.read().splitlines()

        # From left to right
        for line in range(0, len(tree_lines)):
            highest = tree_lines[line][0]
            for column in range(0, len(tree_lines[line])):
                if tree_lines[line][column] > highest:
                    highest = tree_lines[line][column]
                    tree = (line, column)
                    visible_trees.append(tree)

        # From right to left
        tree_lines.reverse()
        for line in range(0, len(tree_lines)):
            highest = tree_lines[line][0]
            for column in range(0, len(tree_lines[line])):
                if tree_lines[line][column] > highest:
                    highest = tree_lines[line][column]
                    tree = (line, column)
                    visible_trees.append(tree)

main()
