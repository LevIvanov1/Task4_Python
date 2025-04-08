def append_to_file(text, filename):

    with open(filename, "a") as file:
        file.write(text + "\n")
    with open(filename, "r") as file:
        lines = file.readlines()
    for index, line in enumerate(lines):
        if (index + 1) % 2 == 0:
            print(line.strip())

append_to_file("Пятая строка", "example.txt")

# В корневой папке example.txt