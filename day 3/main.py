lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_priority(char):
    if char in lowercase:
        return lowercase.index(char)+1
    return uppercase.index(char)+27


def split_string(string):
    length = round(len(string)/2)
    comp1 = string[:length]
    comp2 = string[length:]
    return comp1, comp2


def part1():
    with open("input.txt", mode="r", encoding="utf8") as file:
        rucksacks = file.read().splitlines()
        total = 0
        for rucksack in rucksacks:
            comp1, comp2 = split_string(rucksack)
            already_found = ""
            for char in comp1:
                if char in comp2 and char not in already_found:
                    already_found += char
                    total += get_priority(char)
        print(total)


def part2():
    with open("input.txt", mode="r", encoding="utf8") as file:
        rucksacks = file.read().splitlines()
        total = 0
        for i in range(0, len(rucksacks), 3):
            group = rucksacks[i:i+3]
            for char in group[0]:
                if char in group[1] and char in group[2]:
                    total += get_priority(char)
                    break
        print(total)

#part1()
part2()
