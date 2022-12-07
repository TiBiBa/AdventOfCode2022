def get_folder_size(current_name, folders):
    size = 0
    for name, file_size in folders[current_name].items():
        if file_size == "dir":
            size += get_folder_size(name, folders)
        else:
            size += int(file_size)
    return size


def main():
    with open("input.txt", mode="r", encoding="utf8") as file:
        folders = {}
        folder_structure = []

        lines = file.read().splitlines()
        for line in lines:
            commands = line.split()
            if commands[0] == "$":
                if commands[1] == "cd":
                    if commands[2] == "..":
                        folder_structure = folder_structure[:-1]
                    elif commands[2] == "/":
                        folder_structure = ["/"]
                    else:
                        folder_structure.append(commands[2])
                elif commands[1] == "ls":
                    if folders.get(folder_structure[-1]):
                        print("Deze folder bestaat al!")
                    else:
                        folders[folder_structure[-1]] = folders.get(folder_structure[-1]) or {}
            else:
                folders[folder_structure[-1]][commands[1]] = commands[0]

    folder_sizes = {}
    print(folders)
    for folder, subfiles in folders.items():
        folder_sizes[folder] = get_folder_size(folder, folders)

    total = 0
    for name, size in folder_sizes.items():
        if size <= 100000:
            print(f"{name} - {size}")
            total += size
    print(total)

main()