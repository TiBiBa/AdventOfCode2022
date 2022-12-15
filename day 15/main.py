def split_line(line):
    sensor, beacon = line.split(":")
    sensor_x, sensor_y = sensor.split(",")
    beacon_x, beacon_y = beacon.split(",")

    sensor_x = eval(sensor_x.split("=")[1])
    sensor_y = eval(sensor_y.split("=")[1])

    beacon_x = eval(beacon_x.split("=")[1])
    beacon_y = eval(beacon_y.split("=")[1])

    return (sensor_x, sensor_y), (beacon_x, beacon_y)


def main():
    sensors = []
    beacons = []

    with open("test.txt", mode="r", encoding="utf8") as file:
        lines = file.read().splitlines()
        for line in lines:
            sensor, beacon = split_line(line)
            sensors.append(sensor)
            beacons.append(beacon)


main()