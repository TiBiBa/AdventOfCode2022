import numpy as np


def get_rock_coordinates(rocks):
    coordinates = []
    for rock in rocks:
        parts = rock.split("->")
        for i in range(0, len(parts) - 1):
            x1, y1 = [eval(n) for n in parts[i].split(",")]
            x2, y2 = [eval(n) for n in parts[i + 1].split(",")]
            if x1 == x2:
                bound = 1 if y2 > y1 else -1
                for j in range(y1, y2 + bound, bound):
                    coordinate = [x1, j]
                    coordinates.append(coordinate)
            else:
                bound = 1 if x2 > x1 else -1
                for j in range(x1, x2 + bound, bound):
                    coordinate = [j, y1]
                    coordinates.append(coordinate)
    return coordinates


def get_cave_depth(coordinates):
    depth = 0
    for coordinate in coordinates:
        if coordinate[1] > depth:
            depth = coordinate[1]
    return depth + 1


def get_cave_width(coordinates):
    width = [coordinates[0][0], coordinates[0][0]]
    for coordinate in coordinates:
        if coordinate[0] < width[0]:
            width[0] = coordinate[0]
        elif coordinate[0] > width[1]:
            width[1] = coordinate[0]
    return width


def get_move(cave, grain):
    if cave[grain[1] + 1][grain[0]] == ".":
        return [grain[1] + 1, grain[0]]
    elif cave[grain[1] + 1][grain[0] - 1] == ".":
        return [grain[1] + 1, grain[0] - 1]
    elif cave[grain[1] + 1][grain[0] + 1] == ".":
        return [grain[1] + 1, grain[0] + 1]


def main():
    with open("input.txt", mode="r", encoding="utf8") as file:
        rocks = file.read().splitlines()
        rock_coordinates = get_rock_coordinates(rocks)
        depth = get_cave_depth(rock_coordinates)
        width = get_cave_width(rock_coordinates)

        # Part 1
        cave = np.full((depth, width[1] + 1), ".", dtype=str)
        for coordinate in rock_coordinates:
            cave[coordinate[1], coordinate[0]] = "#"

        units = 0
        try:
            while True:
                units += 1
                grain = [500, -1]
                move = get_move(cave, grain)
                while move:
                    if grain[1] >= 0:
                        cave[grain[1], grain[0]] = "."
                    cave[move[0], move[1]] = "x"
                    grain = [move[1], move[0]]
                    move = get_move(cave, grain)
        except IndexError:
            print(units - 1)

        INFINITY_BOTTOM = 999999
        # Part 2
        cave = np.full((depth+2, INFINITY_BOTTOM), ".", dtype=str)
        for coordinate in rock_coordinates:
            cave[coordinate[1], coordinate[0]] = "#"
        # Add the bottom row
        for i in range(0, INFINITY_BOTTOM):
            cave[depth+1, i] = "#"

        units = 0
        while cave[0, 500] != "x":
            units += 1
            grain = [500, -1]
            move = get_move(cave, grain)
            while move:
                if grain[1] >= 0:
                    cave[grain[1], grain[0]] = "."
                cave[move[0], move[1]] = "x"
                grain = [move[1], move[0]]
                move = get_move(cave, grain)
        print(units)


main()
