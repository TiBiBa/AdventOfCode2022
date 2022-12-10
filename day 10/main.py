import textwrap


def main():
    cycle = 1
    x_value = 1
    relevant_cycles = [20, 60, 100, 140, 180, 220]
    with open("input.txt", mode="r", encoding="utf8") as file:
        cycle_values = {}
        instructions = file.read().splitlines()
        for instruction in instructions:
            instruction = instruction.split()
            if instruction[0] == "noop":
                cycle_values[cycle] = x_value
                cycle += 1
            else:
                for _ in range(0,2):
                    cycle_values[cycle] = x_value
                    cycle += 1
                x_value += int(instruction[1])

    # Part 1
    total = 0
    for cycle in relevant_cycles:
        total += cycle * cycle_values.get(cycle)
    print(total)

    # Part 2
    crt = ""
    for cycle, value in cycle_values.items():
        pos = (cycle-1) % 40
        sprite = [value-1, value, value+1]
        if pos in sprite:
            crt += "#"
        else:
            crt += " "
    crt = textwrap.wrap(crt, 40)
    for row in crt:
        print(row)


main()

