sensors = set()
beacons = set()


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


def main(part1):
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

        # Part 1
        y_points = set()
        y_target = 2000000

        if part1:
            for coordinate, distance in travels.items():
                y_distance = abs(coordinate[1] - y_target)
                if y_distance < distance:
                    y_rest = distance - y_distance
                    for i in range(y_rest+1):
                        point_l = (coordinate[0] - i, y_target)
                        point_r = (coordinate[0] + i, y_target)
                        if point_l not in sensors and point_l not in beacons:
                            y_points.add(point_l)
                        if point_r not in sensors and point_r not in beacons:
                            y_points.add(point_r)

            points = []
            for point in y_points:
                if point[1] == y_target:
                    points.append(point[0])
            print(len(points))
        else:
            out_of_bounds = {}
            for point, distance in travels.items():
                points = [(point[0] + distance, point[1]), (point[0] - distance, point[1]),
                          (point[0], point[1] + distance), (point[0], point[1] - distance)]
                for out_of_bound_point in points:
                    if out_of_bound_point[0] < 0 or out_of_bound_point[0] > 20:
                        pass
                    elif out_of_bound_point[1] < 0 or out_of_bound_point[1] > 20:
                        pass
                    else:
                        if out_of_bounds.get(out_of_bound_point):
                            out_of_bounds[out_of_bound_point] += 1
                        else:
                            out_of_bounds[out_of_bound_point] = 1
        print(out_of_bounds)


main(part1=False)