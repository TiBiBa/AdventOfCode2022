def check_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0

    if isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            check = check_order(left[i], right[i])
            if check != 0:
                return check
        return check_order(len(left), len(right))

    if isinstance(left, int) and isinstance(right, list):
        return check_order([left], right)
    if isinstance(left, list) and isinstance(right, int):
        return check_order(left, [right])


def main():
    with open("input.txt", mode="r", encoding="utf8") as file:
        lines = file.read().splitlines()
        packets = []
        for i in range(0, len(lines), 3):
            packets.append(lines[i: i + 2])

        total = 0
        for i, packet in enumerate(packets):
            left = eval(packet[0])
            right = eval(packet[1])
            if check_order(left, right) < 0:
                total += i + 1

        # Part 1
        print(total)

        # Part 2
        packets = [eval(line) for line in lines if line]
        packets.append(eval('[[2]]'))
        packets.append(eval('[[6]]'))

        # Bubble sort
        for i in range(len(packets)-1):
            for j in range(0, len(packets)-i-1):
                if check_order(packets[j], packets[j + 1]) > -1:
                    packets[j], packets[j + 1] = packets[j + 1], packets[j]

        index_2 = 0
        index_6 = 0
        for index, packet in enumerate(packets):
            if packet == [[2]]:
                index_2 = index + 1
            if packet == [[6]]:
                index_6 = index + 1
        print(index_2 * index_6)
main()
