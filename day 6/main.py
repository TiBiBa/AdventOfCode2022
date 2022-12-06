def main(distinct=4):
    with open("input.txt", mode="r", encoding="utf8") as file:
        datastream = file.read()
        for i in range(0, len(datastream) - (distinct - 1)):
            current_packet = datastream[i:i + distinct]
            if len(set(current_packet)) == len(current_packet):
                # We have to get the end of the packets, as we start at 0 count + distinct
                print(i + distinct)
                break


main(distinct=14)

