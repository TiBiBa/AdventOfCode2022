def create_crate_structure(crates):
    crates_stack = {}
    for crate_line in crates:
        for i in range(0, len(crate_line), 4):
            line_number = round(i / 4 + 1)
            for char in crate_line[i:i + 4]:
                if char.isalpha():
                    if crates_stack.get(line_number):
                        crates_stack[line_number] = [char] + crates_stack.get(line_number)
                    else:
                        crates_stack[line_number] = [char]
    return crates_stack


def split_instructions(instruction):
    instruction = instruction.split()
    amount = instruction[1]
    start = instruction[3]
    loc = instruction[5]

    return int(amount), int(start), int(loc)


def part1():
    with open("input.txt", mode="r", encoding="utf8") as file:
        data = file.read().splitlines()
        crates = data[:8]
        instructions = data[10:]

        crates = create_crate_structure(crates)

        for instruction in instructions:
            amount, start, loc = split_instructions(instruction)

            current_crates = list(crates.get(start)[-amount:])
            current_crates = list(reversed(current_crates))
            crates[start] = crates.get(start)[:-amount]
            crates[loc] = crates.get(loc) + current_crates
        key = ""
        for i in range(1, len(crates)+1):
            key += crates[i][-1]
        print(key)


def part2():
    with open("input.txt", mode="r", encoding="utf8") as file:
        data = file.read().splitlines()
        crates = data[:8]
        instructions = data[10:]

        crates = create_crate_structure(crates)

        for instruction in instructions:
            amount, start, loc = split_instructions(instruction)

            current_crates = list(crates.get(start)[-amount:])
            crates[start] = crates.get(start)[:-amount]
            crates[loc] = crates.get(loc) + current_crates
        key = ""
        for i in range(1, len(crates)+1):
            key += crates[i][-1]
        print(key)


#part1()
part2()