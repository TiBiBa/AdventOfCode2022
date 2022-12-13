def check_order_old(left, right):
    for i, item in enumerate(left):
        if i >= len(right):
            return False
        if isinstance(item, int) and isinstance(right[i], int):
            if item < right[i]:
                return True
            elif item > right[i]:
                return False
            return check_order(left[i + 1:], right[i + 1:])
        if isinstance(item, list) and isinstance(right[i], list):
            for index, x in enumerate(item):
                if index >= len(right[i]) or x > right[i][index]:
                    return False
                if x < right[i][index]:
                    return True
            return check_order(left[i + 1:], right[i + 1:])
        if isinstance(item, list) and isinstance(right[i], int):
            return check_order(item, [right[i]])
        if isinstance(item, int) and isinstance(right[i], list):
            return check_order([item], right[i])
    return True


def check_order(left, right):
    # Check the int case
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif right > left:
            return False

    # Check the double list case
    if isinstance(left, list) and isinstance(right, list):
        for i in range(0, len(left)):
            if i >= len(right):
                return True
            if check_order(left[i], right[i]):
                return True

    # Check the one list, one int case
    if isinstance(left, list) and isinstance(right, int):
        return check_order(left, [right])
    if isinstance(left, int) and isinstance(right, list):
        return check_order([left], right)


def main():
    with open("test.txt", mode="r", encoding="utf8") as file:
        lines = file.read().splitlines()
        packets = []
        for i in range(0, len(lines), 3):
            packets.append(lines[i: i +2])

        total = 0
        for i, packet in enumerate(packets):
            left = eval(packet[0])
            right = eval(packet[1])

            if check_order(left, right):
                print(f"In the correct order: {i + 1}")
                total += i + 1

        # Part 1
        print(total)

main()
