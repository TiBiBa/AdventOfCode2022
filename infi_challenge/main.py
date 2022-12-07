class Santa:
    def __init__(self):
        self.direction = 0
        self.posX = 0
        self.posY = 0

    def change_direction(self, change):
        self.direction = (self.direction + change) % 360

    def move(self, distance):
        # We can hard-code this as the turns are always % 45 and the diagonal distance is simplified
        if self.direction == 0:
            self.posY += distance
        elif self.direction == 45:
            self.posX += distance
            self.posY += distance
        elif self.direction == 90:
            self.posX += distance
        elif self.direction == 135:
            self.posX += distance
            self.posY -= distance
        elif self.direction == 180:
            self.posY -= distance
        elif self.direction == 225:
            self.posX -= distance
            self.posY -= distance
        elif self.direction == 270:
            self.posY -= distance
        elif self.direction == 315:
            self.posX -= distance
            self.posY += distance
        else:
            print("Dit zou niet mogen!")
            exit(1)

    def get_location(self):
        return self.posX, self.posY

    def get_direction(self):
        return self.direction

    def get_distance(self):
        return abs(self.posX) + abs(self.posY)


def main():
    santa = Santa()

    with open("input.txt", mode="r", encoding="utf8") as file:
        instructions = file.read().splitlines()
        for instruction in instructions:
            command, value = instruction.split()
            value = int(value)
            if command == "draai":
                santa.change_direction(value)
            if command == "loop" or command == "spring":
                santa.move(value)

        print(santa.get_location())
        print(santa.get_distance())


main()
