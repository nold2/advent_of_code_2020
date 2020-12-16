file = open("resource.txt", "r")
data = file.readlines()


def part_1():
    counter = 0

    for d in data:
        dirty_range, dirty_character, dirty_password = d.split(" ")
        min, max = [int(val) for val in dirty_range.split("-")]
        char, _ = dirty_character.split(":")
        password, _ = dirty_password.split("\n")

        if min <= password.count(char) <= max:
            counter += 1
    print(counter)


if __name__ == "__main__":
    part_1()
