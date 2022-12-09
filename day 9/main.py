def move_head(pos, direction):
    if direction == "R":
        pos = [pos[0] + 1, pos[1]]
    elif direction == "D":
        pos = [pos[0], pos[1] - 1]
    elif direction == "L":
        pos = [pos[0] - 1, pos[1]]
    else:
        pos = [pos[0], pos[1] + 1]
    return pos


def move_tail(pos_t, pos_h):
    if pos_t[0] == pos_h[0]:
        if pos_t[1] == pos_h[1] + 2:
            pos_t[1] -= 1
        elif pos_t[1] == pos_h[1] - 2:
            pos_t[1] += 1
    elif pos_t[1] == pos_h[1]:
        if pos_t[0] == pos_h[0] + 2:
            pos_t[0] -= 1
        elif pos_t[0] == pos_h[0] - 2:
            pos_t[0] += 1
    else:
        if pos_t[0] == pos_h[0] + 1 and pos_t[1] == pos_h[1] + 1:
            return pos_t
        elif pos_t[0] == pos_h[0] + 1 and pos_t[1] == pos_h[1] - 1:
            return pos_t
        elif pos_t[0] == pos_h[0] - 1 and pos_t[1] == pos_h[1] + 1:
            return pos_t
        elif pos_t[0] == pos_h[0] - 1 and pos_t[1] == pos_h[1] - 1:
            return pos_t
        else:
            if pos_h[0] > pos_t[0] and pos_h[1] > pos_t[1]:
                pos_t = [pos_t[0] + 1, pos_t[1] + 1]
            elif pos_h[0] > pos_t[0] and pos_h[1] < pos_t[1]:
                pos_t = [pos_t[0] + 1, pos_t[1] - 1]
            elif pos_h[0] < pos_t[0] and pos_h[1] < pos_t[1]:
                pos_t = [pos_t[0] - 1, pos_t[1] - 1]
            elif pos_h[0] < pos_t[0] and pos_h[1] > pos_t[1]:
                pos_t = [pos_t[0] - 1, pos_t[1] + 1]
    return pos_t


def main():
    with open("input.txt", mode="r", encoding="utf8") as file:
        pos_h = [0, 0]
        pos_t = {}
        visited_1 = set()
        visited_9 = set()

        for i in range(1, 10):
            pos_t[i] = [0, 0]

        instructions = file.read().splitlines()
        for instruction in instructions:
            direction, length = instruction.split()
            for i in range(0, int(length)):
                pos_h = move_head(pos_h, direction)
                pos_t[1] = move_tail(pos_t[1], pos_h)
                for j in range(2, 10):
                    pos_t[j] = move_tail(pos_t[j], pos_t[j - 1])

                visited_1.add(tuple(pos_t[1]))
                visited_9.add(tuple(pos_t[9]))
        print(len(visited_1))
        print(len(visited_9))


main()
