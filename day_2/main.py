file = open("resource.txt", "r")
data = file.readlines()


def parser(d):
    dirty_range, dirty_character, dirty_password = d.split(" ")

    min, max = [int(val) for val in dirty_range.split("-")]
    char, _ = dirty_character.split(":")
    password, _ = dirty_password.split("\n")

    return min, max, char, password


def part_1():
    counter = 0

    for d in data:
        min, max, char, password = parser(d)
        if min <= password.count(char) <= max:
            counter += 1
    print(counter)


def part_2():
    counter = 0
    for d in data:
        position_first, position_second, char, password = parser(d)
        try:
            if password[position_first - 1] == char and password[position_second - 1] == char:
                continue

            if password[position_first - 1] == char or password[position_second - 1] == char:
                counter += 1
        except ValueError:
            continue

    print(counter)


if __name__ == "__main__":
    part_1()
    part_2()
