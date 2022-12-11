import math

from tqdm import tqdm


class Monkey:
    def __init__(self, items: list, operator: str, test: int, true_target: int, false_target: int):
        self.inspected = 0
        self.worry_reduction = True
        self.items = items
        self.operator = operator
        self.test = test
        self.true_target = true_target
        self.false_target = false_target

    def update_worry_reduction(self, reduction):
        self.worry_reduction = reduction

    def append_item(self, item):
        self.items.append(item)

    def inspect_items(self, lcm):
        targets = []
        for item in self.items:
            new_value = self.calculate_value(item)
            if self.worry_reduction:
                new_value = math.floor(new_value / 3)
            else:
                new_value = new_value % lcm
            target = str(self.get_target(new_value))
            temp = (target, new_value)
            targets.append(temp)
            self.inspected += 1
        self.items = []
        return targets

    def calculate_value(self, old):
        return eval(self.operator)

    def get_target(self, value):
        if value % self.test == 0:
            return self.true_target
        return self.false_target

    def get_test(self):
        return self.test

    def get_inspected(self):
        return self.inspected


def create_monkey(monkey_lines: list):
    id = monkey_lines[0].split(":")[0][-1]
    items = [eval(i) for i in monkey_lines[1].split(":")[1].split(",")]
    operator = monkey_lines[2].split(":")[1].split("=")[1]
    test_value = int(monkey_lines[3].split()[-1])
    true_target = int(monkey_lines[4].split()[-1])
    false_target = int(monkey_lines[5].split()[-1])

    monkey = Monkey(items, operator, test_value, true_target, false_target)
    return id, monkey


# https://theprogrammingexpert.com/python-least-common-multiple/
def lcm(lst):
    lcm_temp = max(lst)
    while True:
        if all(lcm_temp % x == 0 for x in lst):
            break
        lcm_temp = lcm_temp + 1
    return lcm_temp


def main(worry_reduction, rounds):
    rounds = rounds
    monkeys = {}

    with open("input.txt", mode="r", encoding="utf8") as file:
        lines = file.read().splitlines()
        for i in range(0, len(lines), 7):
            current_monkey = lines[i:i + 7]
            monkey_id, monkey = create_monkey(current_monkey)
            monkeys[monkey_id] = monkey
            if not worry_reduction:
                monkeys[monkey_id].update_worry_reduction(worry_reduction)

    # For part 2 we need the LCM to keep the values manage-able but don't lose any info
    divisors = []
    for index, monkey in monkeys.items():
        divisors.append(monkey.get_test())
    LCM = lcm(divisors)

    for _ in tqdm(range(0, rounds)):
        for index, monkey in monkeys.items():
            for target in monkey.inspect_items(LCM):
                monkeys[target[0]].append_item(target[1])

    values = []
    for index, monkey in monkeys.items():
        values.append(monkey.get_inspected())

    max1, max2 = sorted(values, reverse=True)[:2]
    print(max1 * max2)


# Part 1
main(worry_reduction=True, rounds=20)

# Part 2
main(worry_reduction=False, rounds=10000)
