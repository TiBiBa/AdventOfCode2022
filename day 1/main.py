def main():
    with open("input.txt", mode="r", encoding="utf8") as file:
        calories_list = []
        content = file.read().splitlines()
        calories = 0
        for line in content:
            try:
                line = int(line)
                calories += line
            except ValueError:
                calories_list.append(calories)
                calories = 0

        # Part 1
        print(max(calories_list))

        # Part 2
        top3 = [max(calories_list)]
        calories_list.remove(max(calories_list))
        top3.append(max(calories_list))
        calories_list.remove(max(calories_list))
        top3.append(max(calories_list))

        print(sum(top3))


if __name__ == "__main__":
    main()
