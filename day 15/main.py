sensors = set()
beacons = set()
non_beacon = set()


def split_line(line):
    sensor, beacon = line.split(":")
    sensor_x, sensor_y = sensor.split(",")
    beacon_x, beacon_y = beacon.split(",")

    sensor_x = eval(sensor_x.split("=")[1])
    sensor_y = eval(sensor_y.split("=")[1])

    beacon_x = eval(beacon_x.split("=")[1])
    beacon_y = eval(beacon_y.split("=")[1])

    return (sensor_x, sensor_y), (beacon_x, beacon_y)


def manhattan_distance(sensor, beacon):
    distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    return distance


def travel_sensor(coordinate, distance):
    points = [(coordinate[0], coordinate[1] + 1), (coordinate[0] + 1, coordinate[1]),
              (coordinate[0], coordinate[1] - 1), (coordinate[0] - 1, coordinate[1])]

    for point in points:
        non_beacon.add(point)
        travel_sensor(point, distance - 1)


def main():
    global sensors
    global beacons
    travels = {}

    with open("test.txt", mode="r", encoding="utf8") as file:
        lines = file.read().splitlines()
        for line in lines:
            sensor, beacon = split_line(line)
            sensors.add(sensor)
            beacons.add(beacon)
            travels[sensor] = manhattan_distance(sensor, beacon)

        for coordinate, distance in travels.items():
            travel_sensor(coordinate, distance)


main()