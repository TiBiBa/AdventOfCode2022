def split_assignments(pair):
    elf1, elf2 = pair.split(",")
    elf1 = elf1.split("-")
    elf2 = elf2.split("-")
    return elf1, elf2


def check_include(elf1, elf2):
    tasks1 = set(range(int(elf1[0]), int(elf1[1])+1))
    tasks2 = set(range(int(elf2[0]), int(elf2[1])+1))
    if tasks1.issubset(tasks2) or tasks2.issubset(tasks1):
        return True
    return False

def check_overlap(elf1, elf2):
    tasks1 = set(range(int(elf1[0]), int(elf1[1]) + 1))
    tasks2 = set(range(int(elf2[0]), int(elf2[1]) + 1))
    if len(tasks1.intersection(tasks2)) > 0:
        return True
    return False

def part1():
    with open("input.txt", mode="r", encoding="utf8") as file:
        pairs = file.read().splitlines()
        total = 0
        for pair in pairs:
            elf1, elf2 = split_assignments(pair)
            if check_include(elf1, elf2):
                total += 1
        print(total)


def part2():
    with open("input.txt", mode="r", encoding="utf8") as file:
        pairs = file.read().splitlines()
        total = 0
        for pair in pairs:
            elf1, elf2 = split_assignments(pair)
            if check_overlap(elf1, elf2):
                total += 1
        print(total)

#part1()
part2()